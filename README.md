# solarterms
This small python programme is to accurately calculate the times (to millisecond) of 24 [solar terms](https://en.wikipedia.org/wiki/Solar_term)
using [JPL HORIZONS](https://ssd.jpl.nasa.gov/).
本python程式利用噴射推進實驗室的[HORIZONS](https://ssd.jpl.nasa.gov/)网上天文数据精确计算24节气时间（精确到毫秒）。

## Installation
Install Python 3 (and its pip) and download the whole repository to your computer. 

Install required python packages using the following command
```
pip install -r requirements.txt
```

## Usage
For usage, please see test.py
```
$ python3 test.py 
Getting solar terms from JPL HORIZONS. Please wait...
Solar terms for 2020 are (in NZDT):
           datetime           ObsEclLon
----------------------------- ---------
2020-Jan-06 10:30:07.610 NZDT     285.0
2020-Jan-21 03:54:41.322 NZDT     300.0
2020-Feb-04 22:03:21.051 NZDT     315.0
2020-Feb-19 17:57:01.327 NZDT     330.0
2020-Mar-05 15:56:54.422 NZDT     345.0
2020-Mar-20 16:49:38.258 NZDT       0.0
2020-Apr-04 20:38:11.359 NZDT      15.0
2020-Apr-20 03:45:30.125 NZDT      30.0
2020-May-05 13:51:24.482 NZDT      45.0
2020-May-21 02:49:18.348 NZDT      60.0
2020-Jun-05 17:58:27.000 NZDT      75.0
2020-Jun-21 10:43:42.000 NZDT      90.0
2020-Jul-07 04:14:28.509 NZDT     105.0
2020-Jul-22 21:36:53.554 NZDT     120.0
2020-Aug-07 14:06:12.481 NZDT     135.0
2020-Aug-23 04:44:56.973 NZDT     150.0
2020-Sep-07 17:08:04.000 NZDT     165.0
2020-Sep-23 02:30:40.122 NZDT     180.0
2020-Oct-08 08:55:16.859 NZDT     195.0
2020-Oct-23 11:59:33.412 NZDT     210.0
2020-Nov-07 12:13:56.344 NZDT     225.0
2020-Nov-22 09:39:46.517 NZDT     240.0
2020-Dec-07 05:09:31.406 NZDT     255.0
2020-Dec-21 23:02:21.440 NZDT     270.0
```
