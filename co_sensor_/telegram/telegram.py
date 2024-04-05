# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

import asyncio

telegramRecipientsList = {
  "gautam": 6172380644,
  "gautam2": 6126761617,
  "abhilash": 57804912,
  "chauhan" : 6151616867
}
  
# get your api_id, api_hash, token
# from telegram as described above
api_id = '24118763'
api_hash = '08b9b0201e6e13c5006af3a9e2e866a5'
token = '6093155096:AAGTdFXqtWPVsDJbOZJwpdZLAfaXvr5qb0g'
# message = "Working..."
 
# your phone number
phone = '+919321261352'
  
# creating a telegram session and assigning
# it to a variable client

client = TelegramClient('session', api_id, api_hash)
# connecting and building the session
# client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
# if not client.is_user_authorized():

#     client.send_code_request(phone)
    
#     # signing in the client
#     client.sign_in(phone, input('Enter the code: '))


def connect():
    try:
        # connecting and building the session
        client.connect()
        
        # in case of script ran first time it will
        # ask either to input token or otp sent to
        # number or sent or your telegram id
        if not client.is_user_authorized():
            
            client.send_code_request(phone)
            
            # signing in the client
            client.sign_in(phone, input('Enter the code: '))
        
        return
    except Exception as e:
        print(e)
        return


def send_msg(msg,name_arr:list,img):

    print(name_arr)
    if not client.is_connected():
        connect()
    
    for name in name_arr:
        print(name)
        try:

            telegram_id = telegramRecipientsList[name]
            print(name + '=' + str(telegram_id))
            # receiver user_id and access_hash, use
            # my user_id and access_hash for reference
            # receiver = InputPeerUser(6172380644, 0)
            receiver = InputPeerUser(telegram_id, 0)
        
            # sending message using telegram client
            # client.send_message(receiver, msg, parse_mode='html')
            client.send_file(
                        receiver, img , caption=msg, link_preview=True, parse_mode='html'
                    )
        except Exception as e:
            
            # there may be many error coming in while like peer
            # error, wrong access_hash, flood_error, etc
            print(e)
 
    # disconnecting the telegram session
    client.disconnect()