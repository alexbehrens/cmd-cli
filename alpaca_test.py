import pull_alpaca
import setup
import main_cli
import os
import alpaca_trade_api as tradeapi


name = os.environ.get('paca_name')
api_key = os.environ.get('paca_api_key')
api_secret = os.environ.get('paca_api_secret')
password = os.environ.get('paca_password')
base_url = 'https://paper-api.alpaca.markets'

#prev login should be triggered by a csv log file existing
prev_login = True
if prev_login == True:
    main_cli.commands(name, api_key, api_secret, base_url)

if prev_login == False:
    setup.first_setup()