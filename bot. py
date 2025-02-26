from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7313362001:AAH4uqEnyJY3SozQSBde1kPWL05Nyt3kCK8"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Salom! Men sizning Telegram botingizman!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
