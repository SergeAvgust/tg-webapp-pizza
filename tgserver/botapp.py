from settings import TG_TOKEN
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, WebAppInfo
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
import json

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with a button that opens a the web app."""
    await update.message.reply_text(
        "Please press the button below to choose a color via the WebApp.",
        reply_markup=ReplyKeyboardMarkup.from_button(
            KeyboardButton(
                text="Open the color picker!",
                web_app=WebAppInfo(url="https://sergeavgust.github.io/tg-webapp-bot/"),
            ),
            resize_keyboard=True
        ),
        
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Print the received data and remove the button."""
    data = json.loads(update.effective_message.web_app_data.data)
    await update.message.reply_html(text=data)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


bot = ApplicationBuilder().token(TG_TOKEN).build()
    
start_handler = CommandHandler('start', start)
web_app_data_handler = MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
bot.add_handler(start_handler)
bot.add_handler(web_app_data_handler)
bot.add_handler(echo_handler)

async def bot_setup(args):
    await bot.initialize()
    await bot.start()
    await bot.updater.start_polling()
    print('Bot started')

    yield

    print('Closing Bot')
    await bot.updater.stop()
    await bot.stop()
    await bot.shutdown()
    print('Bot Closed')