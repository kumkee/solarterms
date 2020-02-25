import solarterms
import datetime

year = 2020
dt = datetime.timedelta(days=366)
t = datetime.datetime(year, 1, 1, tzinfo=datetime.timezone.utc)
st = solarterms.SolarTerms(baseTime=t, backspan=datetime.timedelta(), forwardspand=dt)

print('Solar terms for {year} are (in {tz}):'.format(year=year, tz=st.tzname()))
print(st)
