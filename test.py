import solarterms
import datetime
import arrow

year = 2020
dt = datetime.timedelta(days=366)
t = arrow.Arrow(year, 1, 1, tzinfo='Pacific/Auckland')
st = solarterms.SolarTerms(baseTime=t, backspan=datetime.timedelta(), forwardspand=dt)

print('Solar terms for {year} are (in {tz}):'.format(year=year, tz=st.tzname()))
print(st)
