print('STARTING BSV PROCESS')

import os 
import time
import robin_stocks as rs
import math
import sys
import random
import datetime

rs.login(username='', password=(''), expiresIn=86400, by_sms=True)
sellSize = 0
buySize = 0
buySize = random.randint(15,17)
sellSize = random.randint(5,7)
change = 0
oldChange = 0

runChecks = [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140,144,148,152,156,160,164,168,172,176,180,184,188,192,196,200,204,208,212,216,220,224,228,232,236,240,244,248,252,256,260,264,268,272,276,280,284,288,292,296,300,304,308,312,316,320,324,328,332,336,340,344,348,352,356,360,364,368,372,376,380,384,388,392,396,400,404,408,412,416,420,424,428,432,436,440,444,448,452,456,460,464,468,472,476,480,484,488,492,496,500,504,508,512,516,520,524,528,532,536,540,544,548,552,556,560,564,568,572,576,580,584,588,592,596,600,604,608,612,616,620,624,628,632,636,640,644,648,652,656,660,664,668,672,676,680,684,688,692,696,700,704,708,712,716,720,724,728,732,736,740,744,748,752,756,760,764,768,772,776,780,784,788,792,796,800,804,808,812,816,820,824,828,832,836,840,844,848,852,856,860,864,868,872,876,880,884,888,892,896,900,904,908,912,916,920,924,928,932,936,940,944,948,952,956,960,964,968,972,976,980,984,988,992,996,1000,1004,1008,1012,1016,1020,1024,1028,1032,1036,1040,1044,1048,1052,1056,1060,1064,1068,1072,1076,1080,1084,1088,1092,1096,1100,1104,1108,1112,1116,1120,1124,1128,1132,1136,1140,1144,1148,1152,1156,1160,1164,1168,1172,1176,1180,1184,1188,1192,1196,1200,1204,1208,1212,1216,1220,1224,1228,1232,1236,1240,1244,1248,1252,1256,1260,1264,1268,1272,1276,1280,1284,1288,1292,1296,1300,1304,1308,1312,1316,1320,1324,1328,1332,1336,1340,1344,1348,1352,1356,1360,1364,1368,1372,1376,1380,1384,1388,1392,1396,1400,1404,1408,1412,1416,1420,1424,1428,1432,1436,1440,1444,1448,1452,1456,1460,1464,1468,1472,1476,1480,1484,1488,1492,1496,1500,1504,1508,1512,1516,1520,1524,1528,1532,1536,1540,1544,1548,1552,1556,1560,1564,1568,1572]
runChecks0 = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,360,362,364,366,368,370,372,374,376,378,380,382,384,386,388,390,392,394,396,398,400,402,404,406,408,410,412,414,416,418,420,422,424,426,428,430,432,434,436,438,440,442,444,446,448,450,452,454,456,458,460,462,464,466,468,470,472,474,476,478,480,482,484,486,488,490,492,494,496,498,500,502,504,506,508,510,512,514,516,518,520,522,524,526,528,530,532,534,536,538,540,542,544,546,548,550,552,554,556,558,560,562,564,566,568,570,572,574,576,578,580,582,584,586,588,590,592,594,596,598,600,602,604,606,608,610,612,614,616,618,620,622,624,626,628,630,632,634,636,638,640,642,644,646,648,650,652,654,656,658,660,662,664,666,668,670,672,674,676,678,680,682,684,686,688,690,692,694,696,698,700,702,704,706,708,710,712,714,716,718,720,722,724,726,728,730,732,734,736,738,740,742,744,746,748,750,752,754,756,758,760,762,764,766,768,770,772,774,776,778,780,782,784,786,788,790,792,794,796,798,800,802,804,806,808,810,812,814,816,818,820,822,824,826,828,830,832,834,836,838,840,842,844,846,848,850,852,854,856,858,860,862,864,866,868,870,872,874,876,878,880,882,884,886,888,890,892,894,896,898,900,902,904,906,908,910,912,914,916,918,920,922,924,926,928,930,932,934,936,938,940,942,944,946,948,950,952,954,956,958,960,962,964,966,968,970,972,974,976,978,980,982,984,986,988,990,992,994,996,998,1000,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056,1058,1060,1062,1064,1066,1068,1070,1072,1074,1076,1078,1080,1082,1084,1086,1088,1090,1092,1094,1096,1098,1100,1102,1104,1106,1108,1110,1112,1114,1116,1118,1120,1122,1124,1126,1128,1130,1132,1134,1136,1138,1140,1142,1144,1146,1148,1150,1152,1154,1156,1158,1160,1162,1164,1166,1168,1170,1172,1174,1176,1178,1180,1182,1184,1186,1188,1190,1192,1194,1196,1198,1200,1202,1204,1206,1208,1210,1212,1214,1216,1218,1220,1222,1224,1226,1228,1230,1232,1234,1236,1238,1240,1242,1244,1246,1248,1250,1252,1254,1256,1258,1260,1262,1264,1266,1268,1270,1272,1274,1276,1278,1280,1282,1284,1286,1288,1290,1292,1294,1296,1298,1300,1302,1304,1306,1308,1310,1312,1314,1316,1318,1320,1322,1324,1326,1328,1330,1332,1334,1336,1338,1340,1342,1344,1346,1348,1350,1352,1354,1356,1358,1360,1362,1364,1366,1368,1370,1372,1374,1376,1378,1380,1382,1384,1386,1388,1390,1392,1394,1396,1398,1400,1402,1404,1406,1408,1410,1412,1414,1416,1418,1420,1422,1424,1426,1428,1430,1432,1434,1436,1438,1440,1442,1444,1446,1448,1450,1452,1454,1456,1458,1460,1462,1464,1466,1468,1470,1472,1474,1476,1478,1480,1482,1484,1486,1488,1490,1492,1494,1496,1498,1500,1502,1504,1506,1508,1510,1512,1514,1516,1518,1520,1522,1524,1526,1528,1530,1532,1534,1536,1538,1540,1542,1544,1546,1548,1550,1552,1554,1556,1558,1560,1562,1564,1566,1568,1570,1572,1574,1576,1578,1580,1582,1584,1586,1588,1590,1592,1594,1596,1598,1600,1602,1604,1606,1608,1610,1612,1614,1616,1618,1620,1622,1624,1626,1628,1630,1632,1634,1636,1638,1640,1642,1644,1646,1648,1650,1652,1654,1656,1658,1660,1662,1664,1666,1668,1670,1672,1674,1676,1678,1680,1682,1684,1686,1688,1690,1692,1694,1696,1698,1700,1702,1704,1706,1708,1710,1712,1714,1716,1718,1720,1722,1724,1726,1728,1730,1732,1734,1736,1738,1740,1742,1744,1746,1748,1750,1752,1754,1756,1758,1760,1762,1764,1766,1768,1770,1772,1774,1776,1778,1780,1782,1784,1786,1788,1790,1792,1794,1796,1798,1800,1802,1804,1806,1808,1810,1812,1814,1816,1818,1820,1822,1824,1826,1828,1830,1832,1834,1836,1838,1840,1842,1844,1846,1848,1850,1852,1854,1856,1858,1860,1862,1864,1866,1868,1870,1872,1874,1876,1878,1880,1882,1884,1886,1888,1890,1892,1894,1896,1898,1900,1902,1904,1906,1908,1910,1912,1914,1916,1918,1920,1922,1924,1926,1928,1930,1932,1934,1936,1938,1940,1942,1944,1946,1948,1950,1952,1954,1956,1958,1960,1962,1964,1966,1968,1970,1972,1974,1976,1978,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010,2012,2014,2016,2018,2020,2022,2024,2026,2028,2030,2032,2034,2036,2038,2040,2042,2044,2046,2048,2050,2052,2054,2056,2058,2060,2062,2064,2066,2068,2070,2072,2074,2076,2078,2080,2082,2084,2086,2088,2090,2092,2094,2096,2098,2100,2102,2104,2106,2108,2110,2112,2114,2116,2118,2120,2122,2124,2126,2128,2130,2132,2134,2136,2138,2140,2142,2144,2146,2148,2150,2152,2154,2156,2158,2160,2162,2164,2166,2168,2170,2172,2174,2176,2178,2180,2182,2184,2186,2188,2190,2192,2194,2196,2198,2200,2202,2204,2206,2208,2210,2212,2214,2216,2218,2220,2222,2224,2226,2228,2230,2232,2234,2236,2238,2240,2242,2244,2246,2248,2250,2252,2254,2256,2258,2260,2262,2264,2266,2268,2270,2272,2274,2276,2278,2280,2282,2284,2286,2288,2290,2292,2294,2296,2298,2300,2302,2304,2306,2308,2310,2312,2314,2316,2318,2320,2322,2324,2326,2328,2330,2332,2334,2336,2338,2340,2342,2344,2346,2348,2350,2352,2354,2356,2358,2360,2362,2364,2366,2368,2370,2372,2374,2376,2378,2380,2382,2384,2386,2388,2390,2392,2394,2396,2398,2400,2402,2404,2406,2408,2410,2412,2414,2416,2418,2420,2422,2424,2426,2428,2430,2432,2434,2436,2438,2440,2442,2444,2446,2448,2450,2452,2454,2456,2458,2460,2462,2464,2466,2468,2470,2472,2474,2476,2478,2480]
runChecks2 = [3,4,5,6,10,11,12,13,14,18,19,20,21,23,25,26,28,30,31,33,34,36,37,39,41,42,44,45,47,49,50,52,53,55,57,58,60,61,63,65,66,68,69,71,73,74,76,77,79,81,82,84,85,87,88,90,92,93,95,96,98,100,101,103,104,106,108,109,111,112,114,116,117,119,120,122,124,125,127,128,130,132,133,135,136,138,139,141,143,144,146,147,149,151,152,154,155,157,159,160,162,163,165,167,168,170,171,173,175,176,178,179,181,182,184,186,187,189,190,192,194,195,197,198,200,202,203,205,206,208,210,211,213,214,216,218,219,221,222,224,226,227,229,230,232,233,235,237,238,240,241,243,245,246,248,249,251,253,254,256,257,259,261,262,264,265,267,269,270,272,273,275,277,278,280,281,283,284,286,288,289,291,292,294,296,297,299,300,302,304,305,307,308,310,312,313,315,316,318,320,321,323,324,326,327,329,331,332,334,335,337,339,340,342,343,345,347,348,350,351,353,355,356,358,359,361,363,364,366,367,369,371,372,374,375,377,378,380,382,383,385,386,388,390,391,393,394,396,398,399,401,402,404,406,407,409,410,412,414,415,417,418,420,422,423,425,426,428,429,431,433,434,436,437,439,441,442,444,445,447,449,450,452,453,455,457,458,460,461,463,465,466,468,469,471,472,474,476,477,479,480,482,484,485,487,488,490,492,493,495,496,498,500,501,503,504,506,508,509,511,512,514,516,517,519,520,522,523,525,527,528,530,531,533,535,536,538,539,541,543,544,546,547,549,551,552,554,555,557,559,560,562,563,565,567,568,570,571,573,574,576,578,579,581,582,584,586,587,589,590,592,594,595,597,598,600,602,603,605,606,608,610,611,613,614,616,617,619,621,622,624,625,627,629,630,632,633,635,637,638,640,641,643,645,646,648,649,651,653,654,656,657,659,661,662,664,665,667,668,670,672,673,675,676,678,680,681,683,684,686,688,689,691,692,694,696,697,699,700,702,704,705,707,708,710,712,713,715,716,718,719,721,723,724,726,727,729,731,732,734,735,737,739,740,742,743,745,747,748,750,751,753,755,756,758,759,761,762,764,766,767,769,770,772,774,775,777,778,780,782,783,785,786,788,790,791,793,794,796,798,799,801,802,804,806,807,809,810,812,813,815,817,818,820,821,823,825,826,828,829,831,833,834,836,837,839,841,842,844,845,847,849,850,852,853,855,857,858,860,861,863,864,866,868,869,871,872,874,876,877,879,880,882,884,885,887,888,890,892,893,895,896,898,900,901,903,904,906,907,909,911,912,914,915,917,919,920,922,923,925,927,928,930,931,933,935,936,938,939,941,943,944,946,947,949,951,952,954,955,957,958,960,962,963,965,966,968,970,971,973,974,976,978,979,981,982,984,986,987,989,990,992,994,995,997,998,1000,1002,1003,1005,1006,1008,1009,1011,1013,1014,1016,1017,1019,1021,1022,1024,1025,1027,1029,1030,1032,1033,1035,1037,1038,1040,1041,1043,1045,1046,1048,1049,1051,1052,1054,1056,1057,1059,1060,1062,1064,1065,1067,1068,1070,1072,1073,1075,1076,1078,1080,1081,1083,1084,1086,1088,1089,1091,1092,1094,1096,1097,1099,1100,1102,1103,1105,1107,1108,1110,1111,1113,1115,1116,1118,1119,1121,1123,1124,1126,1127,1129,1131,1132,1134,1135,1137,1139,1140,1142,1143,1145,1147,1148,1150,1151,1153,1154,1156,1158,1159,1161,1162,1164,1166,1167,1169,1170,1172,1174,1175,1177,1178,1180,1182]
runChecks3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601]

change = float(rs.get_crypto_quote('BSV')['mark_price'])
    
g=10
l=1
while l > 0:
    old = 0
    discountedBSVAverage = 0
    BSV_Average = 0
    sleep1 = 0
    sleep2 = 0
    nowMark = 0
    old = 0
    old1 = 0
    thisBuySize = 0
    l = l + 1
    avgVolume15sec1hrAvg = 0
    avgVolume10minute1hrAvg = 0
    minus10PCT_10min = 0
    PLUS10PCT_10min = 0
    PLUS10PCT_15second = 0
    minus10PCT_15second = 0
    cryptoBuyingPower = 0 
    BSV_Average = BSV_Average + 1
    
    #5min day
    i_15sec1hrAvg = rs.crypto.get_crypto_historicals('BSV', '5minute', 'day')
    raw_15sec1hrAvg = float(old/len(i_15sec1hrAvg))

    #10min week
    i_10minute1hrAvg = rs.crypto.get_crypto_historicals('BSV', '10minute', 'week')
    raw_10minute1hrAvg = float(old1/len(i_10minute1hrAvg))

    #hour week
    i_hourWeekAvg = rs.crypto.get_crypto_historicals('BSV', 'hour', 'week')    
    raw_hourWeekAvg = float(old1/len(i_hourWeekAvg))

    #hour month
    i_hourMonthAvg = rs.crypto.get_crypto_historicals('BSV', 'hour', 'month')    
    raw_hourMonthAvg = float(old1/len(i_hourMonthAvg))

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    #determine change
    nowMark = float(rs.get_crypto_quote('BSV')['mark_price'])    
    print(time.sleep(random.randint(15,17)))

    ####
    print('Start BSV Loop - Count: ',l)
    print('>Price of BSV @ ',current_time,': ',nowMark)
    print('>>Price of BSV @ ',current_time,':',change)
    print('>>>Previous Price of BSV @ ',current_time,':',oldChange)
    print('>BSV raw_15sec1hrAvg @ ',current_time,': ',raw_15sec1hrAvg)
    print('>BSV raw_10minute1hrAvg @ ',current_time,': ',raw_10minute1hrAvg)

    #Sizing Logic 
    mod0 = 1
    mod1 = 1
    mod2 = 1
    mod3 = 1
    mod4 = 1
    mod5 = 1
    
    
    #buy size mod
    cryptoBuyingPower = float(((rs.profiles.load_account_profile(info="crypto_buying_power")).replace("'","")))
    print('Crypto Buying Power: ',cryptoBuyingPower) 
    
    if cryptoBuyingPower > 5000: 
        mod5 = 2
    else:
        if cryptoBuyingPower > 2500: 
            mod5 = 1.5
        else: 
            if cryptoBuyingPower > 1000: 
                mod5 = 1.25
            else: 
                if cryptoBuyingPower > 100: 
                    mod5 = 1.1
                else: 
                    mod5 = .75
    
    #day of week mod
    curDay = datetime.datetime.today().weekday()
    baseBuySize = ((random.randint(21,25)))
    baseSellSize = ((random.randint(5,7))) 

    #price action mod
    #default sleep values
    sleep1 = round((random.randint(60,120)),0)
    sleep2 = round((random.randint(121,180)),0)
    nowMark = float(rs.get_crypto_quote('BSV')['mark_price'])

    if raw_10minute1hrAvg < raw_hourMonthAvg:
        print('..raw_10minute1hrAvg < raw_hourMonthAvg')
        baseBuySize = ((random.randint(21,25)))
        baseSellSize = ((random.randint(5,7)))  
        #come back sooner if fastAverage is below slowAverage
        sleep1 = round((random.randint(60,120)),0)
        sleep2 = round((random.randint(121,133)),0)
    else: 
        print('..raw_10minute1hrAvg > raw_hourMonthAvg')
        baseBuySize = ((random.randint(5,7)))
        baseSellSize = ((random.randint(21,25)))
        #wait a while if fastAverage is above slowAverage 
        sleep1 = round((random.randint(150,200)),0)
        sleep2 = round((random.randint(201,255)),0)

    if raw_15sec1hrAvg < raw_10minute1hrAvg:
        print('..raw_15sec1hrAvg < raw_10minute1hrAvg')
        baseBuySize = ((random.randint(21,25)))
        baseSellSize = ((random.randint(5,7)))  
        #come back sooner if fastAverage is below slowAverage
        sleep1 = round((random.randint(60,120)),0)
        sleep2 = round((random.randint(121,133)),0)
    else: 
        print('..raw_15sec1hrAvg > raw_10minute1hrAvg')
        baseBuySize = ((random.randint(5,7)))
        baseSellSize = ((random.randint(21,25)))
        #wait a while if fastAverage is above slowAverage 
        sleep1 = round((random.randint(150,200)),0)
        sleep2 = round((random.randint(201,255)),0)
        
    if nowMark < raw_15sec1hrAvg:
        print('..nowMark < raw_hourWeekAvg')
        baseBuySize = ((random.randint(21,25)))
        baseSellSize = ((random.randint(5,7)))  
        #come back sooner if nowPrice is spiking down
        sleep1 = round((random.randint(60,120)),0)
        sleep2 = round((random.randint(121,133)),0)
    else: 
        print('..nowMark > raw_hourWeekAvg')
        baseBuySize = ((random.randint(5,7)))
        baseSellSize = ((random.randint(21,25)))
        #wait a while if nowPrice is spiking up 
        sleep1 = round((random.randint(150,200)),0)
        sleep2 = round((random.randint(201,255)),0)

    if nowMark < raw_15sec1hrAvg:
        print('..nowMark < raw_15sec1hrAvg')
        baseBuySize = ((random.randint(21,25)))
        baseSellSize = ((random.randint(5,7)))  
        #come back sooner if nowPrice is spiking down
        sleep1 = round((random.randint(60,120)),0)
        sleep2 = round((random.randint(121,133)),0)
    else: 
        print('..nowMark > raw_15sec1hrAvg')
        baseBuySize = ((random.randint(5,7)))
        baseSellSize = ((random.randint(21,25)))

        #wait a while if nowPrice is spiking up 
        sleep1 = round((random.randint(150,200)),0)
        sleep2 = round((random.randint(201,255)),0)

    if nowMark < raw_15sec1hrAvg:
        print('..nowMark < raw_15sec1hrAvg')
        baseBuySize = ((random.randint(21,25)))
        baseSellSize = ((random.randint(5,7)))  
        #come back sooner if nowPrice is spiking down
        sleep1 = round((random.randint(60,120)),0)
        sleep2 = round((random.randint(121,133)),0)
    else: 
        print('..nowMark > raw_15sec1hrAvg')
        baseBuySize = ((random.randint(5,7)))
        baseSellSize = ((random.randint(21,25)))
        #wait a while if nowPrice is spiking up 
        sleep1 = round((random.randint(150,200)),0)
        sleep2 = round((random.randint(201,255)),0)

    buySize = baseBuySize
    sellSize = baseSellSize

    print('>BSV - buySize: ',buySize)
    print('>BSV - sellSize: ',sellSize)

    if nowMark > change:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        rs.orders.order_sell_crypto_by_price('BSV',3,timeInForce='gtc')            

        print('<>BSV change > oldChange: Sell $',3,' @ ',current_time,' at Price: $',change,'<>')
        
        nowMark = float(rs.get_crypto_quote('BSV')['mark_price'])

        if l in runChecks:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            rs.orders.order_sell_crypto_by_price('BSV',sellSize,timeInForce='gtc')    
            
            change = float(rs.get_crypto_quote('BSV')['mark_price'])
            print('<>BSV nowMark > raw_10minute1hrAvg: SELL - $',sellSize,' & SLEEP random(',sleep1,' & ',sleep2,') @ ',current_time,' at Price: $',change,'<>')
            #print('<>BSV nowMark > raw_10minute1hrAvg: SLEEP random(',sleep1,' & ',sleep2,') @ ',current_time,' at Price: $',change,'<>')
            print(time.sleep(random.randint(sleep1,sleep2)))
        else: 
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            change = float(rs.get_crypto_quote('BSV')['mark_price'])    

            print('<>BSV nowMark > raw_10minute1hrAvg: SLEEP random(',sleep1,' & ',sleep2,') @ ',current_time,' at Price: $',change,'<>')
            print(time.sleep(random.randint(sleep1,sleep2)))    
    else: 
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        rs.orders.order_buy_crypto_by_price('BSV',7,timeInForce='gtc')
        change = float(rs.get_crypto_quote('BSV')['mark_price'])
        print('<>BSV change < oldChange: BUY - $',7,' @ ',current_time,' at Price: $',change,'<>')
        nowMark = float(rs.get_crypto_quote('BSV')['mark_price'])
    
        if l in runChecks3:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            
            #rs.orders.order_buy_crypto_by_price('BSV',buySize,timeInForce='gtc')
            change = float(rs.get_crypto_quote('BSV')['mark_price'])
            print('<>BSV nowMark < raw_15sec1hrAvg: BUY - $',buySize,' & SLEEP random(',sleep1,' & ',sleep2,') @ ',current_time,' at Price: $',change,'<>')
            #print('<>BSV nowMark < raw_15sec1hrAvg: SLEEP random(',sleep1,' & ',sleep2,') @ ',current_time,' at Price: $',change,'<>')
            print(time.sleep(random.randint(sleep1,sleep2)))
        else: 
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print('<>BSV nowMark > raw_15sec1hrAvg: SLEEP random(',sleep1,' & ',sleep2,') @ ',current_time,' at Price: $',change,'<>')
            print(time.sleep(random.randint(sleep1,sleep2)))
            