import requests

bot_api_key = '5854610426:AAF2F6aBmlNXnEUoG-Lzub7VR19UlNY21JU'
group_chat_id = '-1001833665419'
def send_to_telegram(message,img,channel_id='-1001833665419'):
    # response = requests.get(f'https://api.telegram.org/bot{bot_api_key}/sendMessage', { 
    #     'chat_id': group_chat_id, 
    #     'text': message,
    #     'parse_mode' : 'html'})
    # if response.status_code == 200:
    #     print('Telegram Message Sent Succesfully')
    # else: print(response.text) # Do what you want with response
    # return
    try:
        photo_url = f'https://www.octopus-automation.com/apps/eqi/images/telegram/{img}'
        print(photo_url)
        response = requests.get(f'https://api.telegram.org/bot{bot_api_key}/sendPhoto', { 
            'chat_id': channel_id,
            'photo' :  photo_url,
            'caption': message,
            'parse_mode' : 'html'})
        if response.status_code == 200:
            print('Telegram Message Sent Succesfully')
        else: print(response.text) # Do what you want with response
        return
    except:
        print("Error Sending Telegram Notification")

# send_to_telegram("hello from python")
# send_to_telegram("<b>Quantum Diesel Generator</b>\n" + "Quantum Diesel Generator 1" + " switched On","dg.jpg")