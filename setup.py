import pull_alpaca
from selenium import webdriver



def first_setup():
    #first check if csv exists
    print ('')
    print ('')
    print ('')
    print ('================================================')
    print ("💹 Welcome to the Securities Exchange Command Line Interface (SECLI)")
    print ('')
    print ('')
    print ('')
    print ('================================================')
    name = input("👤  Enter what you want to be called: ")
    print ('')
    print ('')
    print ('')
    print ('================================================')
    print ("👤  Welcome", name)
    print ('')
    print ('')
    print ('')
    print ('================================================')
    psd_str = str("🔐  Create a Password: ")
    pwd = input(psd_str)
    print ('')
    print ('')
    print ('')
    print ('================================================')
    pwd_confirm = input("🔐  Re-enter Password: ")

    print ('')
    print ('')
    print ('')
    print ('================================================')
    paca = input('🦙  Do you have an Alpaca account? (y/n) ')


    #save name password and paca to protected? json file


    if paca.lower() == 'y':
        print ('')
        print ('')
        print ('')
        print ('================================================')
        api_key = input('🦙  Please enter your Alpaca API Key: ')
        print ('')
        print ('')
        print ('')
        print ('================================================')
        print ('🦙  Confirm Alpaca API Key: '+api_key)
        api_key_confirm = input('(y/n): ')
        if api_key_confirm == 'y':
            print ('')
            print ('')
            print ('')
            print ('================================================')
            api_secret = input('🦙  Please enter your Alpaca API Secret: ')
            print ('')
            print ('')
            print ('')
            print ('================================================')
            print ('🦙  Confirm Alpaca API Secret: '+api_secret)
            print ('')
            print ('')
            print ('')
            print ('================================================')
            api_key_confirm = input('(y/n): ')
        else:
            api_key = input('Please enter your Alpaca API Key: ')
            print ('Confirm Alpaca API Key: '+api_secret)
            api_key_confirm = input('(y/n): ')
            #need to fix this part of the loop
        pull_alpaca.paca_login(api_key,api_secret)
        
            
        


    if paca == 'n':
        print ('')
        print ('')
        print ('')
        print ('================================================')
        print ('🦙  Would you like to sign up for an Alpaca Account?: ')
        api_key_confirm = input('(y/n): ')
        if api_key_confirm == 'y':
            print ('')
            print ('')
            print ('')
            print ('================================================')
            driver = webdriver.Firefox()
            driver.get("https://app.alpaca.markets/signup")
        if api_key_confirm == 'n':
            print ('')
            print ('')
            print ('')
            print ('================================================')
            print ('🤷‍♀️ You should probably get with the program')

    

