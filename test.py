import solarterms
import datetime
import arrow
import sys
import pandas as pd

pd.set_option('display.max_rows', 30)

year = int(sys.argv[1]) if len(sys.argv) >=2 else 2021
dt = datetime.timedelta(days=366)
tz = sys.argv[2] if len(sys.argv) >=3 else 'Australia/Sydney'
t = arrow.Arrow(year, 1, 1, tzinfo=tz)
st = solarterms.SolarTerms(baseTime=t, backspan=datetime.timedelta(), forwardspand=dt)

print('Solar terms for {year} will be (in the timezone of {tz}):'.format(year=year, tz=st.tzname()))
print(st)
