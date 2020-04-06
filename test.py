import solarterms
import datetime
import arrow

year = 2021
dt = datetime.timedelta(days=366)
t = arrow.Arrow(year, 1, 1, tzinfo='Australia/Sydney')
st = solarterms.SolarTerms(baseTime=t, backspan=datetime.timedelta(), forwardspand=dt)

print('Solar terms for {year} will be (in the timezone of {tz}):'.format(year=year, tz=st.tzname()))
print(st)
