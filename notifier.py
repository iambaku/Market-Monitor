import os
from telegram import Bot
bot=Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
CHAT_ID=os.getenv("TELEGRAM_CHAT_ID")
async def send_report(text,files):
 for file in files:
  with open(file,"rb") as f:
   await bot.send_photo(chat_id=CHAT_ID,photo=f)
 await bot.send_message(chat_id=CHAT_ID,text=text)
