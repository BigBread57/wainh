from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from src.settings import config

storage = MemoryStorage()

bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot, storage=storage)

DATABASES = {
    'drivername': 'postgresql',
    'database': config('DATABASE'),
    'username': config('USERNAME'),
    'password': config('PASSWORD'),
    'host': config('HOST'),
    'port': config('PORT'),
}
