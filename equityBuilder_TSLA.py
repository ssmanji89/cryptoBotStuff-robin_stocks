print("STARTING TSLA PROCESS")

import os 
import time
import robin_stocks as rs
import math
import sys
import random

rs.login(username="", password=(""), expiresIn=86400, by_sms=True)

sellSize = 1
buySize = 1
i_15sec1hrAvg = '';
buySize = random.randint(5,7)
sellSize = random.randint(5,7)
change = 0
oldChange = 0

oldChange = str(rs.stocks.get_latest_price("TSLA", includeExtendedHours=True)[0])

l=1
while True:
    old = 0
    discountedTSLAAverage = 0
    TSLA_Average = 0
    nowMark = 0
    old = 0
    old1 = 0
    l = l + 1
    avgVolume15sec1hrAvg = 0
    avgVolume10minute1hrAvg = 0
    minus10PCT_10min = 0
    PLUS10PCT_10min = 0
    PLUS10PCT_15second = 0
    minus10PCT_15second = 0

    print('Start TSLA Loop - Count: ',l)
    l=l+1
    TSLA_Yesterday_Close = str(rs.stocks.get_stock_quote_by_symbol("TSLA", info=None)['previous_close'])
    TSLA_Today_Open = str(rs.stocks.get_stock_quote_by_symbol("TSLA", info=None)['last_trade_price'])
    print('(TSLA_Today_Open < TSLA_Yesterday_Close) Returns: ',(TSLA_Today_Open < TSLA_Yesterday_Close))
    buySize = random.randint(1,3)
    sellSize = random.randint(3,5)
    sleepsBuy = random.randint(599,727)
    sleepsSell = random.randint(307,503)
    sleepNone = random.randint(900,1800)
    
    if (TSLA_Today_Open < TSLA_Yesterday_Close): 

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        print(time.sleep(random.randint(15,37)))
        change = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])

        print("Start TSLA Loop - Count: ",l)
        print(">Price of TSLA @ ",current_time,": ",oldChange)
        print(">>Price of TSLA @ ",current_time,":",change)
        print(">>>Previous Price of TSLA @ ",current_time,":",oldChange)

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)  
        change = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])        
        print("Today < Yesterday - ",current_time," at Price: $",change," then SLEEP for ",sleepNone," seconds<>")

        if change > oldChange:
            print("TSLA Change less than OldChange: THEN")
            oldChange = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])
            print("<>TSLA change > oldChange: SELL $2 @ ",current_time," at Price: $",change," then SLEEP for ",sleepsBuy,"<>")    
            time.sleep(sleepNone)
        else: 
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("<>TSLA change < oldChange: BUY ",buySize," @ ",current_time," at Price: $",change," then SLEEP for ",sleepsSell,"<>")
            rs.orders.order_buy_fractional_by_price("TSLA",buySize,timeInForce="gfd",extendedHours="false")                
            time.sleep(sleepsBuy)
    else:
        change = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])
        if change > oldChange:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)  
            print("Today > Yesterday - SLEEP @ ",current_time," at Price: $",change," then SLEEP for ",sleepNone," seconds<>")
            change = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])
            time.sleep(sleepNone)           
        else:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("Today > Yesterday and change < oldChange - BUY $1 @ ",current_time," at Price: $",change," then SLEEP for ",sleepsBuy," seconds<>")
            rs.orders.order_buy_fractional_by_price("TSLA",buySize,timeInForce="gfd",extendedHours="false")
            oldChange = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])
            change = str((rs.stocks.get_latest_price("TSLA", includeExtendedHours=True))[0])
            time.sleep(sleepsBuy)
