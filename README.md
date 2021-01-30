# manavakcina-notify-bot

Python script that is supposed to give an edge in Latvia's Covid vaccine registration program. 
The vaccination website will add registration function in a few days and earlier registration will mean better place in queue compared to other people in the same group.

How the script works:
1) Checks HTML code length of 'manavakcina.lv' homepage
2) Compares it to previous result
3) Sends a message to Telegram channel if there have been changes

After every change, there is a possibility that registration button has been added to the site.

Deployed on RPi as cron job that runs every 5 minutes.
