import os
from telethon.sync import TelegramClient
from dotenv import load_dotenv

load_dotenv()
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
PHONE = os.environ.get("PHONE")


def sendMessage(receiver, message):

    # creating a telegram session and assigning
    # it to a variable client
    client = TelegramClient("session", API_ID, API_HASH)

    # connecting and building the session
    client.connect()

    # in case of script ran first time it will
    # ask either to input token or otp sent to
    # number or your telegram id
    if not client.is_user_authorized():
        client.send_code_request(PHONE)

        # signing in the client
        client.sign_in(PHONE, input("Enter the code: "))

    try:

        # sending message using telegram client
        client.send_message(receiver, message)

    except Exception as e:
        print(e)

    # disconnecting the telegram session
    client.disconnect()
