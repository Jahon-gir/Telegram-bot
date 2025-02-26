import time
from datetime import datetime
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7313362001:AAH4uqEnyJY3SozQSBde1kPWL05Nyt3kCK8"  # O'zingizning Telegram bot tok

bot = Bot(token=TOKEN)

# Eslatmalar ro'yxati
reminders = []

def set_reminder(update, context: CallbackContext):
    """Foydalanuvchi eslatma qo'shishi uchun buyruq."""
    try:
        text = " ".join(context.args)
        if not text:
            update.message.reply_text("❗ Iltimos, eslatma matnini yozing. Misol: /reminder 14:30 Kitob o'qish")
            return

        time_part, message = text.split(" ", 1)
        hour, minute = map(int, time_part.split(":"))
        reminder_time = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)

        reminders.append((reminder_time, message))
        update.message.reply_text(f"✅ Eslatma qo'shildi: {message} ({time_part})")

    except Exception as e:
        update.message.reply_text("❌ Xatolik yuz berdi! Formati to'g'ri: /reminder 14:30 Kitob o'qish")
        print(e)

def check_reminders(context: CallbackContext):
    """Har daqiqada eslatmalarni tekshirish."""
    now = datetime.now().replace(second=0, microsecond=0)
    for reminder in reminders[:]:
        if reminder[0] == now:
            context.bot.send_message(chat_id=context.job.context, text=f"⏰ Eslatma: {reminder[1]}")
            reminders.remove(reminder)

def start(update, context):
    """Botni ishga tushirish."""
    update.message.reply_text("👋 Salom! Menga eslatma qo'shishingiz mumkin. Misol: /reminder 14:30 Mashq qilish")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reminder", set_reminder))

    job_queue = updater.job_queue
    job_queue.run_repeating(check_reminders, interval=60, first=0, context=update.message.chat_id)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
