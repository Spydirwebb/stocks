import configparser

from telethon import TelegramClient

def createClient():
    #reading configs
    config = configparser.ConfigParser()
    config.read("config.ini")

    #setting config values
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']

    api_hash = str(api_hash)

    phone = config['Telegram']['phone']
    username = config['Telegram']['username']

    #create the client and connect
    client = TelegramClient(username, api_id, api_hash)

    #return
    return client, phone

