from aiogram.utils import executor
from settings.common import dp
from handlers import start_game


start_game.register_handlers_other(dp)


async def on_startup(_):
    print('Работает')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
