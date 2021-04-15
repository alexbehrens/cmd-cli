import pull_alpaca
import setup
import os
import alpaca_trade_api as tradeapi
import time
import sys

def loading():
    count = [1]
    print ('')
    for i in count:
        for c in ('/', '-', '\\', '|', ' '):
            time.sleep(0.25)
            sys.stdout.write('\b' + c)
            sys.stdout.flush()


loading()


def normal_login(name, api_key, api_secret, password,base_url):
    print ('')
    print ('')
    print ('')
    print(' █▀▄ ▄▀▄ █▀▄ ▄▀▀')
    print(' █▀  █▀█ █▀▄ ▄██')
    print ('')
    print ('')
    print ('')
    print ('================================================')
    print ("💹 Welcome to Pars - the friendly market CLI")
    print ('')
    print ('')
    print ('')
    print ('================================================')
    pwd = input("🔒 Enter Password: ")
    print ('')
    print ('')
    print ('')
    while pwd != password:
        print ('================================================')
        pwd = input("❌ Incorrect Password, Re-enter: ")
        print ('')
        print ('')
        print ('')
    print ('================================================')
    print ('🔓 Password is correct.')
    print ('')
    print ('')
    print ('')
    print ('================================================')
    print ('👋 Welcome back', name)
    print ('')
    print ('')
    print ('')
    print ('================================================')
    pull_alpaca.paca_login(api_key,api_secret,base_url)
    return True
    # welcome name, today is a great/terrible day for you


#historical_data = [9000,10123]
#current_balence  = 10123
#daily_growth = (current_balence-historical_data[0])
#daily_percentage = (daily_growth/current_balence)*100
#block_count = current_balence/10
#plug dummy values with alpaca values
#pull all position data

#print ('================================================')
#print ('🧾 Account Balence: $'+str(current_balence), block_count, 'blocks')
#print ('')
#print ('🌇 Daily Gain: +$'+str(round(daily_growth, 2)), '+'+str(round(daily_percentage, 2))+'%')
#print ('')
#print ('')


def commands(name, api_key, api_secret, base_url):
    base_url = 'https://paper-api.alpaca.markets'
    api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
    #add command menu
    print ('')
    print ('')
    print ('================================================')

    command = input("⚙️  Enter Next Command: ")


    def sell():
        print ('')
        print ('')
        print ('')
        print ('================================================')
        ticker = input("🗂  (Sell) Input Ticker: ").upper()
        print ('')
        print ('')
        print ('')
        print ('================================================')
        shares = input("🔢  (Sell) Input Number of Shares: ")
        share = int(shares)
        print ('')
        print ('')
        print ('')
        print ('================================================')
        print ('🦙  Confirm selling', shares, 'share(s)', 'of', ticker)
        #retrieve number of shares owned of ticker
        api_key_confirm = input('(y/n): ').lower()
        if api_key_confirm == 'y':
            print ('')
            print ('')
            api.submit_order(
                symbol=ticker,
                qty=shares,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            print ('================================================')
            print ('✅ You have sold', shares, 'shares of', ticker)
            print ('⤵️ ',name,'👋 ', ticker)
            command = 'loop'
            #print out total gain/loss of stock since holding



        
        

    def buy():
        print ('')
        print ('')
        print ('')
        print ('================================================')
        ticker = input("🗂  (Buy) Input Ticker: ").upper()
        print ('')
        print ('')
        print ('')
        print ('================================================')
        shares = input("🔢  (Buy) Input Number of Shares: ")
        share = int(shares)
        print ('')
        print ('')
        print ('')
        print ('================================================')
        print ('🦙  Confirm buying', shares, 'share(s)', 'of', ticker)
        api_key_confirm = input('(y/n): ').lower()
        if api_key_confirm == 'y':
            print ('')
            print ('')
            api.submit_order(
                symbol=ticker,
                qty=shares,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            print ('================================================')
            print ('✅  You now own', shares, 'share(s) of', ticker)
            print ('⤴️  ',name,'🤝 ', ticker)
            #print (result.order)
            command = 'loop'


    def all_past_trades():
        closed_orders = api.list_orders(
        status='closed',
        limit=100,
        nested=True  # show nested multi-leg orders
        )
        for i in closed_orders:
            print ('')
            print ('')
            print ('')
            print ('================================================')
            print (i)
            



    def firesale():
        #sell all positions 
        print('firesale')


    #create a dictionary w/ positions
    positions = ['apple', 'Microsoft']
    def view_positions():
        for i in positions:
            print ('i')
            #idea is you print overall and recent stats to weed out longterm/shortterm losers

    while command != 'end' or 'exit' or 'e':
        if command == 'sell':
            sell()
        if command == 'buy':
            buy()
        if command == 'firesale':
            firesale()
        if command == 'positions':
            buy()
        if command == 'trades':
            all_past_trades()
        else:
            print ('')
            print ('')
            print ('================================================')
            command = input("⚙️  Enter Next Command: ")










