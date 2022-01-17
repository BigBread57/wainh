from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

cancel_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
cancel = KeyboardButton('/Отменить')

cancel_buttons.row(cancel)


yes_no_buttons = InlineKeyboardMarkup(row_width=1)
yes = InlineKeyboardButton(text='Да', callback_data='true')
no = InlineKeyboardButton(text='Нет', callback_data='false')

yes_no_buttons.row(yes, no)


view_pause_buttons = InlineKeyboardMarkup(row_width=1)
not_pause = InlineKeyboardButton(text='Без пауз', callback_data='not_pause')
drink = InlineKeyboardButton(text='Разлевайте рюмки и готовьте тосты', callback_data='drink')
tea = InlineKeyboardButton(text='Чайная церемония', callback_data='tea')
music = InlineKeyboardButton(text='Музыкальная пауза', callback_data='music')
other = InlineKeyboardButton(text='Другие развлечения', callback_data='other')

view_pause_buttons.row(not_pause).row(drink).row(tea).row(music).row(other)
