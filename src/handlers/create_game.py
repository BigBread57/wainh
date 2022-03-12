from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from data_base.request_for_db.create_game import get_username
from src.buttons.common_buttons import common_buttons
from src.buttons.settings_buttons import yes_no_buttons, cancel_buttons, view_pause_buttons, cancel_skip_buttons


class FSMNewGame(StatesGroup):
    """Класс конечных автоматов для создания игры."""
    username = State()
    humor = State()
    view_pause = State()
    room = State()


async def create_game(message: types.Message):
    """Создать игру."""
    await FSMNewGame.username.set()
    await message.reply(
        'Для создания комнаты, укажите некоторые настройки игры. ' +
        'Внимание! Создатель игры автоматически становится ведущим.',
        reply_markup=cancel_buttons,
    )

    username_game = await get_username(message.from_user.id)
    if username_game:
        await message.reply(
            f'Укажите новый ник для игры, или используйте {username_game}',
            reply_markup=cancel_skip_buttons)
    else:
        await message.reply('Укажите ник для игры.')


async def username(message: types.Message, state: FSMContext):
    """Запоминаем username игрока."""
    async with state.proxy() as data:
        if message.text == '/Отменить':
            await cancel_create_task(message, state)
        else:

            # СДЕЛАТЬ ПРОВЕРКУ ЕСТЬ ЛИ НИК У ИГРОКА ИЛИ НЕТ
            await message.answer('Добавить юмор в игру?', reply_markup=yes_no_buttons)


async def humor_call(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    """Запоминаем результат выбора настройки юмора."""
    async with state.proxy() as data:
        data['humor'] = callback.data
    await FSMNewGame.next()
    await callback.message.reply(
        'Добавить паузы в игру? ',
        reply_markup=view_pause_buttons,
    )


async def pause_call(
        callback: types.CallbackQuery,
        state: FSMContext,
):
    """Запоминаем результат выбора настройки пауз."""
    async with state.proxy() as data:
        data['view_pause'] = callback.data
    # ФУНКЦИЯ ДЛЯ ЗАНЕСЕНИЯ ДАННЫХ В БД
    # ФУНКЦИЯ ДЛЯ СОЗДАНИЯ КОМНАТЫ И ПЕРЕДАЧА ID КОМНАТЫ
    await state.finish()
    await callback.message.reply(
        'Вы создали игру! '
    )


async def cancel_create_task(message: types.Message, state: FSMContext):
    """Отмена создания игры."""
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вы отменили действие.', reply_markup=common_buttons)


def register_handlers_other(dp: Dispatcher):
    """Регистрация обработчиков."""
    dp.register_message_handler(create_game, commands=['Создать_игру'])
    dp.register_message_handler(username, state=FSMNewGame.username)
    dp.register_callback_query_handler(humor_call, state=FSMNewGame.humor)
    dp.register_callback_query_handler(pause_call, state=FSMNewGame.view_pause)
    dp.register_message_handler(cancel_create_task, state="*", commands=['Отменить'])
    dp.register_message_handler(
        cancel_create_task,
        Text(equals='отменить', ignore_case=True),
        state="*",
    )
