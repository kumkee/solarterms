from astroquery.jplhorizons import Horizons
import datetime
import concurrent.futures
import numpy as np
from astropy import table as atb
from copy import deepcopy
import arrow


minTimeDelta = datetime.timedelta(seconds = 0.5)
zeroTimeDelta = datetime.timedelta()
MaxWorkers = 20
TOLERANCE = 1e-12
#JPLTimeFormat = "%Y-%b-%d %H:%M:%S.%f"
JPLTimeFormat = "YYYY-MMM-DD HH:mm:ss.SSS"
numberOfTerms = 24
degreeOfCircle = 360
lengthOfTermInDegs = degreeOfCircle / numberOfTerms
lengthOfTermInDays = datetime.timedelta(days = 365.25/numberOfTerms + 1)

ColNameEclLon = 'ObsEclLon'
ColNameTimeStr = 'datetime_str'
ColNameTime = 'datetime'


def time2Str(t, withtz=False):
    #format = JPLTimeFormat + " %Z" if withtz else JPLTimeFormat
    if isinstance(t, str):
        return t
    else:
        if withtz:
            return t.format( JPLTimeFormat + " ZZZ" )
        else:
            return t.format(JPLTimeFormat)

def str2Time(str, tz='UTC'):
    if(str.count(':')<2):
        str += ':00'
    if(str.count('.')<1):
        str += '.0'
    return arrow.get(str, JPLTimeFormat, tzinfo=tz)
    #return datetime.datetime.strptime(str, JPLTimeFormat).replace(tzinfo=tz)

def str2Timestamp(str):
    return str2Time(str).float_timestamp
    #return str2Time(str).timestamp()

def timestamp2Time(ts, tz=datetime.timezone.utc):
    return arrow.get(ts, tzinfo=tz)
    #return datetime.datetime.fromtimestamp(ts, tz=tz)

def timestamp2Str(ts):
    return time2Str(timestamp2Time(ts))

#def utcnow():
#    return datetime.datetime.now(tz=datetime.timezone.utc)


def sunHorizons(start, stop, step):
    return Horizons(id='10', location='geo', id_type='majorbody', \
            epochs={'start': time2Str(start), 'stop': time2Str(stop), 'step':step})


def eclipticLongitude(horizons):
    return horizons.ephemerides(quantities='31')[ColNameTimeStr, ColNameEclLon]


def checkSolarTerms(longitudes):
    r = longitudes[ColNameEclLon] % lengthOfTermInDegs
    rd = r[1:] - r[:-1]
    return [i for i, x in enumerate(rd) if x <= 0]


def timespan2StepSize(timespan):
    if timespan < zeroTimeDelta:
        raise ValueError('timespan < zero')
    elif timespan < minTimeDelta:
        raise ValueError('timespan < 0.5s')
    elif timespan > 2*lengthOfTermInDays:
        return '3d'
    elif timespan > datetime.timedelta(days = 1):
        return '1h'
    elif timespan > datetime.timedelta(minutes = 50):
        return '1m'
    else:
        return str(timespan // minTimeDelta)


def horizons2RoughTerms(horizons):
    l = eclipticLongitude(horizons)
    ind = checkSolarTerms(l)
    return [l[i:i+2] for i in ind]


def refineTerm(roughTerm):
    start = roughTerm[ColNameTimeStr][0]
    stop = roughTerm[ColNameTimeStr][1]
    #debug:
    #print('----------------- debug -----------------')
    #print('stop:', stop)
    #print('start:', start)
    tspan = str2Time(stop) - str2Time(start)
    #debug:print('refineTerm is called. start, tspan = ', start, tspan)
    if tspan <= 1.2*minTimeDelta:
        return roughTerm
    step = timespan2StepSize(tspan)
    h = sunHorizons(start, stop, step)
    l = eclipticLongitude(h)
    ind = checkSolarTerms(l)[0]
    return refineTerm(l[ind:ind+2])


def linInterpTerm(term, n=0):
    xp = term[ColNameEclLon]
    if xp[1] - xp[0] < 0:
        xp[0] -= degreeOfCircle
    if xp[0] % lengthOfTermInDegs <= TOLERANCE \
       or abs(lengthOfTermInDegs - xp[0] % lengthOfTermInDegs) <= TOLERANCE \
       or n > 4:
        return term
    start = term[ColNameTimeStr][0]
    stop = term[ColNameTimeStr][1]
    yp = list( map(str2Timestamp, term[ColNameTimeStr]) )
    x = xp[-1] - xp[-1]%lengthOfTermInDegs
    y0 = np.interp(x, xp, yp)
    #debug:print('linInterpTerm is called. start, n, y0 = ', start, n, timestamp2Str(y0))
    t_y0 = timestamp2Time(y0)
    t_2 = t_y0 + minTimeDelta
    h = sunHorizons(t_y0, t_2, '1')
    return linInterpTerm(eclipticLongitude(h), n+1)


class SolarTerms:
    def __init__(self, baseTime = arrow.utcnow(), timespan=2*lengthOfTermInDays, forwardspand=None, backspan=None, tz=None):
        print('Getting solar terms from JPL HORIZONS. Please wait...')
        self.__basetime = baseTime
        #self.__tz = self.__basetime.astimezone().tzinfo if tz is None else tz
        #if not isinstance(self.__tz, datetime.timezone):
        #    raise TypeError('tz must be a datetime.timezone object.')
        if forwardspand is None:
            forwardspand = timespan / 2.0
        if backspan is None:
            backspan = timespan / 2.0
        horizons = sunHorizons(self.__basetime - backspan, self.__basetime + forwardspand, \
                                timespan2StepSize(backspan + forwardspand))
        self.__terms = horizons2RoughTerms(horizons)
        with concurrent.futures.ThreadPoolExecutor(max_workers=MaxWorkers) as executor:
            self.__terms = list( executor.map(refineTerm, self.__terms) )
            self.__terms = list( executor.map(linInterpTerm, self.__terms) )
            self.__terms = atb.Table( rows = list(map( lambda x: x[0], self.__terms )), names=[ColNameTime, ColNameEclLon] )
            self.__terms[ColNameTime] = list( map(str2Time, self.__terms[ColNameTime]) )

    @property
    def tzinfo(self):
        return self.__basetime.tzinfo

    def tzname(self):
        return self.__basetime.datetime.tzname()

    def __repr__(self):
        return self.__terms.__repr__()

    def __str__(self):
        terms = deepcopy(self.__terms)
        terms[ColNameTime] = list( map(lambda x: time2Str(x.to(self.tzinfo), withtz=True), terms[ColNameTime]) )
        return terms.__str__()

    def __getitem__(self, arg):
        return self.__terms.__getitem__(arg)
