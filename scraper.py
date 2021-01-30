# -*- coding: utf-8 -*-
import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from telegram import sendMessage

load_dotenv()
RECEIVER_MAIN = os.environ.get("RECEIVER_MAIN")
RECEIVER_LOGS = os.environ.get("RECEIVER_LOGS")
RECEIVER_ALERT = os.environ.get("RECEIVER_ALERT")

try:
    # scrape full HTML from Manavakcina homepage
    response = requests.get("https://manavakcina.lv/")

    if os.path.isfile("previous.html"):
        # Check and notify if HTML code length in website is different from previous scrape
        previousLength = len(open("previous.html", mode="r", encoding="utf-8").read())
        currentLength = len(response.text)
        if previousLength == currentLength:
            messageContent = "Scrape successful, no changes detected. {}".format(datetime.now().time())
            sendMessage(RECEIVER_LOGS, messageContent)
        else:
            messageContent = "Koda izmaiņas Manavakcīna mājaslapā!"
            sendMessage(RECEIVER_MAIN, messageContent)
    else:
        sendMessage(RECEIVER_LOGS, "First Scrape in this Session")

    # update previous.html with latest scraper data
    file = open("previous.html", mode="w", encoding="utf-8")
    file.write(response.text)
    file.close()

except Exception as e:
    sendMessage(RECEIVER_ALERT, str(e))
