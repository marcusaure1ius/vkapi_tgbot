import logging

from aiogram.dispatcher.filters import Command
from aiogram import types



from bot_loader import dp
from bot_loader import bot

@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    await message.answer(text=f'''
    Привет, {message.from_user.full_name}!\nДанный бот умеет проводить аналитику сообществ из Вконтакте!\nЧтобы начать, запусти поиск сообществ командой /search \n Хочешь посмотреть пример работы бота? Нажми на /demo
    ''')