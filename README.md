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

## Compilation of locale translations
In order for you local translations to work, you will need to compile the po file of your language into its binary mo file. Here is the example of how to do that for ja on linux.
```
$ cd locale/ja/LC_MESSAGES
$ msgfmt -o solarterms.mo solarterms
```
To compile po files on Windows, you can use [poedit](https://poedit.net/).

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
A second example is in Tokyo time and Japanese term names:
```
$ LANGUAGE=ja python test.py 2026 'Asia/Tokyo'
Calculating solar terms from JPL HORIZONS data. Please wait...
Solar terms for 2026 will be (in the timezone of Asia/Tokyo):
          datetime          ObsEclLon term
--------------------------- --------- ----
2026- 1-05 17:23:10.398 JST     285.0   小寒
2026- 1-20 10:44:57.008 JST     300.0   大寒
2026- 2-04 05:02:08.913 JST     315.0   立春
2026- 2-19 00:51:56.449 JST     330.0   雨水
2026- 3-05 22:59:00.103 JST     345.0   啓蟄
2026- 3-20 23:45:58.439 JST       0.0   春分
2026- 4-05 03:40:00.201 JST      15.0   清明
2026- 4-20 10:39:07.517 JST      30.0   穀雨
2026- 5-05 20:48:44.714 JST      45.0   立夏
2026- 5-21 09:36:45.366 JST      60.0   小満
2026- 6-06 00:48:22.909 JST      75.0   芒種
2026- 6-21 17:24:31.300 JST      90.0   夏至
2026- 7-07 10:56:58.281 JST     105.0   小暑
2026- 7-23 04:13:06.044 JST     120.0   大暑
2026- 8-07 20:42:45.300 JST     135.0   立秋
2026- 8-23 11:18:49.181 JST     150.0   処暑
2026- 9-07 23:41:17.964 JST     165.0   白露
2026- 9-23 09:05:13.910 JST     180.0   秋分
2026-10-08 15:29:18.271 JST     195.0   寒露
2026-10-23 18:37:57.077 JST     210.0   霜降
2026-11-07 18:52:05.163 JST     225.0   立冬
2026-11-22 16:23:21.405 JST     240.0   小雪
2026-12-07 11:52:32.330 JST     255.0   大雪
2026-12-22 05:50:15.050 JST     270.0   冬至
```
