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
For usage, please see test.py. An example of running the test.py is listed below, where solar terms are different from those in the Northern Hemisphere.
```
$ python test.py                                                                                                                                                         <<<
Calculating solar terms from JPL HORIZONS data. Please wait...
Solar terms for 2021 will be (in the timezone of Australia/Sydney):
           datetime           ObsEclLon         term        
----------------------------- --------- --------------------
2021-Jan-05 14:23:26.864 AEDT     285.0           Minor Heat
2021-Jan-20 07:39:52.788 AEDT     300.0           Major Heat
2021-Feb-04 01:58:48.889 AEDT     315.0      Start of Autumn
2021-Feb-18 21:43:59.456 AEDT     330.0          End of Heat
2021-Mar-05 19:53:42.094 AEDT     345.0            White Dew
2021-Mar-20 20:37:29.732 AEDT       0.0       Autumn Equinox
2021-Apr-04 23:35:07.429 AEST      15.0             Cold Dew
2021-Apr-20 06:33:25.196 AEST      30.0                Frost
2021-May-05 16:47:11.678 AEST      45.0      Start of Winter
2021-May-21 05:37:08.063 AEST      60.0           Minor Snow
2021-Jun-05 20:52:07.232 AEST      75.0           Major Snow
2021-Jun-21 13:32:11.008 AEST      90.0      Winter Solstice
2021-Jul-07 07:05:29.830 AEST     105.0           Minor Cold
2021-Jul-23 00:26:26.821 AEST     120.0           Major Cold
2021-Aug-07 16:53:59.535 AEST     135.0      Start of Spring
2021-Aug-23 07:34:59.830 AEST     150.0       Spring Showers
2021-Sep-07 19:52:57.303 AEST     165.0 Awakening of Insects
2021-Sep-23 05:21:06.456 AEST     180.0       Spring Equinox
2021-Oct-08 12:39:03.184 AEDT     195.0      Pure Brightness
2021-Oct-23 15:51:11.137 AEDT     210.0           Grain Rain
2021-Nov-07 15:58:46.720 AEDT     225.0      Start of Summer
2021-Nov-22 13:33:44.844 AEDT     240.0           Grain Buds
2021-Dec-07 08:57:04.838 AEDT     255.0         Grain in Ear
2021-Dec-22 02:59:19.364 AEDT     270.0      Summer Solstice
```
