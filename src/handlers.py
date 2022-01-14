from telegram.ext import CommandHandler

from commands import start

start_handler = CommandHandler("start", start)
