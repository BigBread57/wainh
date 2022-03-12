from aiogram import types, Dispatcher

from src.buttons.common_buttons import common_buttons


async def start(message: types.Message):
    """Привественное слово и запуск кнопок."""
    await message.reply('Добро пожаловать в игру!', reply_markup=common_buttons)


async def help_players(message: types.Message):
    """Помощь игрокам."""
    await message.reply(
        'Данный бот создан для организации игры в компании друзей.'
    )


async def rules_game(message: types.Message):
    """Правила игры."""
    await message.reply(
        'Правила игры в разработке!'
    )


async def connect_game(message: types.Message):
    """Подключиться к игре."""
    await message.reply(
        'Для подключения игры введите в следующем сообщением код комнаты.'
    )


async def reading_code_room(message: types.Message):
    """Считывание кода комнаты."""
    if message.text.startswith('room:'):
        print('Ура')


def register_handlers_other(dp: Dispatcher):
    """Регистрация обработчиков."""
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help_players, commands=['Помощь'])
    dp.register_message_handler(rules_game, commands=['Правила_игры'])
    dp.register_message_handler(connect_game, commands=['Подключиться_к_игре'])
    dp.register_message_handler(reading_code_room)
