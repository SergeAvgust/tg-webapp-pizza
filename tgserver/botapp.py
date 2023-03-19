from settings import TG_TOKEN
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


bot = ApplicationBuilder().token(TG_TOKEN).build()
    
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
bot.add_handler(start_handler)
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