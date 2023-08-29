import os
from dotenv import load_dotenv
from telethon.tl.types import InputPeerUser
from telethon import TelegramClient, sync, events
from XiaomiEuRomChecker.auth_app.xiaomi_eu_new_thread_checker import telegram_message

load_dotenv()

# get your api_id, api_hash, token from telegram
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
token = os.getenv('TOKEN')
message = telegram_message()

# your phone number
phone = os.getenv('PHONE_NUMBER')

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))
for m in message:
    try:
        # receiver user_id and access_hash, use
        # my user_id and access_hash for reference
        receiver = InputPeerUser(int(os.getenv('USER_ID')), 0)

        # sending message using telegram client
        client.send_message(entity=os.getenv('CHANNEL_NAME'), message=m)
    except Exception as e:

        # there may be many error coming in while like peer
        # error, wrong access_hash, flood_error, etc
        print(e)

# disconnecting the telegram session
client.disconnect()
