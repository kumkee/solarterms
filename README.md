# solarterms
This small python programme is to accurately calculate the times (to millisecond) of 24 [solar terms](https://en.wikipedia.org/wiki/Solar_term)
using [JPL HORIZONS](https://ssd.jpl.nasa.gov/).
本python程式利用噴射推進實驗室的[HORIZONS](https://ssd.jpl.nasa.gov/)网上天文数据精确计算24节气时间（精确到毫秒）。

## Installation
Install Python 3 (and its pip) and download the whole repository to your computer. 

Install required python packages using the following command
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## HORIZONS' rate limit
HORIZONS has introduced rate limits to their service. To avoid going over the limits, default maximum thread number has been set to 2. If you still encounter timeout error, please wait a moment before performing new calculations. 

## Usage
For usage, please see test.py. An example of running the test.py is listed below, where solar terms are different from those in the Northern Hemisphere.
```
$ source env/bin/activate
$ python test.py 2024 'Australia/Sydney'
Calculating solar terms from JPL HORIZONS data. Please wait...
WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
WARNING: AstropyDeprecationWarning: ``id_type``s 'majorbody' and 'id' are deprecated and replaced with ``None``, which has the same functionality. [astroquery.jplhorizons.core]
Solar terms for 2024 will be (in the timezone of Australia/Sydney):
           datetime           ObsEclLon         term
----------------------------- --------- --------------------
2024-Jan-06 07:49:23.550 AEDT     285.0           Minor Heat
2024-Jan-21 01:07:21.724 AEDT     300.0           Major Heat
2024-Feb-04 19:27:08.603 AEDT     315.0      Start of Autumn
2024-Feb-19 15:13:11.338 AEDT     330.0          End of Heat
2024-Mar-05 13:22:47.198 AEDT     345.0            White Dew
2024-Mar-20 14:06:25.232 AEDT       0.0       Autumn Equinox
2024-Apr-04 18:02:18.815 AEDT      15.0             Cold Dew
2024-Apr-19 23:59:46.598 AEST      30.0                Frost
2024-May-05 10:10:06.214 AEST      45.0      Start of Winter
2024-May-20 22:59:31.491 AEST      60.0           Minor Snow
2024-Jun-05 14:09:54.758 AEST      75.0           Major Snow
2024-Jun-21 06:51:00.836 AEST      90.0      Winter Solstice
2024-Jul-07 00:20:04.400 AEST     105.0           Minor Cold
2024-Jul-22 17:44:26.672 AEST     120.0           Major Cold
2024-Aug-07 10:09:17.336 AEST     135.0      Start of Spring
2024-Aug-23 00:55:03.794 AEST     150.0       Spring Showers
2024-Sep-07 13:11:21.660 AEST     165.0 Awakening of Insects
2024-Sep-22 22:43:40.375 AEST     180.0       Spring Equinox
2024-Oct-08 05:59:58.184 AEDT     195.0      Pure Brightness
2024-Oct-23 09:14:45.284 AEDT     210.0           Grain Rain
2024-Nov-07 09:20:05.465 AEDT     225.0      Start of Summer
2024-Nov-22 06:56:30.694 AEDT     240.0           Grain Buds
2024-Dec-07 02:17:03.601 AEDT     255.0         Grain in Ear
2024-Dec-21 20:20:35.169 AEDT     270.0      Summer Solstice
```
A second example is in Tokyo time and Japanese term names (non-English locale not working as of 2022/01/05) for 2020:
```
$ LANGUAGE=ja python test.py 2020 Asia/Tokyo  
Calculating solar terms from JPL HORIZONS data. Please wait...
Solar terms for 2020 will be (in the timezone of Asia/Tokyo):
          datetime          ObsEclLon term
--------------------------- --------- ----
2020- 1-06 06:30:07.610 JST     285.0   小寒
2020- 1-20 23:54:41.322 JST     300.0   大寒
2020- 2-04 18:03:21.051 JST     315.0   立春
2020- 2-19 13:57:01.327 JST     330.0   雨水
2020- 3-05 11:56:54.422 JST     345.0   啓蟄
2020- 3-20 12:49:38.258 JST       0.0   春分
2020- 4-04 16:38:11.359 JST      15.0   清明
2020- 4-19 23:45:30.125 JST      30.0   穀雨
2020- 5-05 09:51:24.482 JST      45.0   立夏
2020- 5-20 22:49:18.348 JST      60.0   小満
2020- 6-05 13:58:27.000 JST      75.0   芒種
2020- 6-21 06:43:42.000 JST      90.0   夏至
2020- 7-07 00:14:28.509 JST     105.0   小暑
2020- 7-22 17:36:53.554 JST     120.0   大暑
2020- 8-07 10:06:12.481 JST     135.0   立秋
2020- 8-23 00:44:56.973 JST     150.0   処暑
2020- 9-07 13:08:04.000 JST     165.0   白露
2020- 9-22 22:30:40.122 JST     180.0   秋分
2020-10-08 04:55:16.859 JST     195.0   寒露
2020-10-23 07:59:33.412 JST     210.0   霜降
2020-11-07 08:13:56.344 JST     225.0   立冬
2020-11-22 05:39:46.517 JST     240.0   小雪
2020-12-07 01:09:31.406 JST     255.0   大雪
2020-12-21 19:02:21.440 JST     270.0   冬至
```
