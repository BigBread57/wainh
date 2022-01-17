from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

help_me = KeyboardButton('/Помощь')
rules_game = KeyboardButton('/Правила_игры')
create_game = KeyboardButton('/Создать_игру')
connect_game = KeyboardButton('/Подключиться_к_игре')

common_buttons = ReplyKeyboardMarkup(resize_keyboard=True)

common_buttons.row(
    help_me, rules_game,
).row(
    create_game, connect_game,
)
