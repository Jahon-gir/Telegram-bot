import time
import schedule
from telegram import Bot

TOKEN = "7313362001:AAH4uqEnyJY3SozQSBde1kPWL05Nyt3kCK8"
CHAT_ID = "975661145"

bot = Bot(token=TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

# ⏰ Kunlik eslatmalar jadvali
schedule.every().day.at("08:00").do(send_message, "🏋‍♂ Ertalabki mashqlar vaqti!")
schedule.every().day.at("09:00").do(send_message, "💻 Dasturlash vaqti!")
schedule.every().day.at("14:00").do(send_message, "📖 Kitob o‘qish vaqti!")
schedule.every().day.at("18:00").do(send_message, "📈 Biznes yoki trading vaqti!")
schedule.every().day.at("22:00").do(send_message, "🗣 Til o‘rganish vaqti!")

while True:
    schedule.run_pending()
    time.sleep(30)
