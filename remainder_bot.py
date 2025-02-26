from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

TOKEN = "7313362001:AAH4uqEnyJY3SozQSBde1kPWL05Nyt3kCK8"

# Esdaliklar ro‘yxati
reminders = {}

async def start(update: Update, context: CallbackContext) -> None:
    """Foydalanuvchiga bot haqida ma’lumot berish."""
    await update.message.reply_text("Salom! Men eslatmalar botiman.\n"
                                    "Menga /add buyruği bilan eslatma qo‘shing.\n"
                                    "/list buyruği bilan eslatmalaringizni ko‘ring.")

async def add_reminder(update: Update, context: CallbackContext) -> None:
    """Yangi eslatma qo‘shish."""
    chat_id = update.message.chat_id
    if len(context.args) < 2:
        await update.message.reply_text("To‘g‘ri format: /add <vaqt sekundlarda> <matn>")
        return

    try:
        time = int(context.args[0])
        text = " ".join(context.args[1:])
    except ValueError:
        await update.message.reply_text("Iltimos, vaqtni raqamda kiriting.")
        return

    if chat_id not in reminders:
        reminders[chat_id] = []

    reminders[chat_id].append((time, text))
    await update.message.reply_text(f"Eslatma {time} sekunddan keyin yuboriladi: {text}")

    await asyncio.sleep(time)
    await context.bot.send_message(chat_id=chat_id, text=f"Eslatma: {text}")

async def list_reminders(update: Update, context: CallbackContext) -> None:
    """Foydalanuvchiga hozirgi eslatmalarni ko‘rsatish."""
    chat_id = update.message.chat_id
    if chat_id not in reminders or not reminders[chat_id]:
        await update.message.reply_text("Sizda eslatmalar yo‘q.")
        return

    reminder_text = "\n".join([f"{t} sek - {txt}" for t, txt in reminders[chat_id]])
    await update.message.reply_text(f"Sizning eslatmalaringiz:\n{reminder_text}")

def main():
    """Botni ishga tushirish."""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add_reminder))
    app.add_handler(CommandHandler("list", list_reminders))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
