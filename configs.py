# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = 7506821
	API_HASH = "ac6e8365d1a9c9df59dc796fc6cb661f"
	BOT_TOKEN = '6147670183:AAGUcBL8ITKTXV5GAuWsfzm3u8Tsd4ffFDg'
	BOT_USERNAME = "meetghetiyapatel_bot"
	DB_CHANNEL = -1001900157222
	BOT_OWNER = 846546194
	DATABASE_URL ="mongodb+srv://MeetGhetiya:meetgpatel@cluster0.8mil8ub.mongodb.net/"
	UPDATES_CHANNEL = "-1001875647256"
	LOG_CHANNEL = -1001875647256
	BANNED_USERS = set("1234567890")
	FORWARD_AS_COPY = True
	BROADCAST_AS_COPY = False
	BANNED_CHAT_IDS = list("-1001362659779 -1001255795497")
	OTHER_USERS_CAN_SAVE_FILE = True
	ADMINS=[]
	ADMINS.append(BOT_OWNER)
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @AbirHasan2005

👥 **Support Group:** [Linux Repositories](https://t.me/DevsZone)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @AbirHasan2005

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/AbirHasan2005) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
