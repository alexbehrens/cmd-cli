import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
from datetime import datetime
import json


def paca_login(api_key,api_secret, base_url):
#authentication and connection details

    #instantiate REST API
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

    #obtain account information
    account = api.get_account()
    print ('🚦  Alpaca Markets Account Status:', account.status)
    account_dict = str(account)

    buying_power = float(account.buying_power)
    print ('')
    print ('')
    print ('')
    print ('================================================')
    print('💸 Buying power: $'+str(round(buying_power, 2)))
    equity = float(account.equity)
    print('💸 Equity: $'+str(round(equity, 2)))

    closed_orders = api.list_orders(
        status='closed',
        limit=100,
        nested=True  # show nested multi-leg orders
    )
    closed_aapl_orders = [o for o in closed_orders if o.symbol == 'UBER']
    print(type(closed_aapl_orders))  
    print('----') 

    #print(closed_orders)
    order_dict = {}
    for i in closed_aapl_orders:
        print(type(i))
        print(i)
        #print ("-----------------")
        test = str(i)[9:-2]
        #print (test)
        x = test.split(',')
        #print(x)

        for u in x:
            #print (u)
            z = u.split(':')
            #print (z)
            order_dict[z[0]] = z[1]


    #print (order_dict)




        #print (json.loads(test))

        


    return(account)



#dictionary = list(account_dict.split(",") 

#for key in dictionary.items:
    #print(key)


