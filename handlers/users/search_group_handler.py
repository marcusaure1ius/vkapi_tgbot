import logging

from aiogram.dispatcher.filters import Command
from aiogram import types

from keyboards.inline.callback_data import search_callback
from keyboards.inline.search_choice_kb import getSearchResult

from bot_loader import dp
from bot_loader import bot

from stats_analysis import get_group_stats

@dp.message_handler(commands=['search'])
async def search_command_handler(message: types.Message):
    await message.answer(text='Для начала анализа тебе надо выбрать сообщество. Работает это так:\n - Вводишь имя сообщества, можно не полностью\n - Получаешь от 1 до 3 вариантов ответа по твоему запросу\n - Выбираешь нужный вариант для продолжения')


@dp.message_handler()
async def start_search_handler(message: types.Message):
    await message.answer(text=f'Ты выбрал для поиска "{message.text}". Вот что я нашел для тебя:', reply_markup=getSearchResult(message.text))


@dp.callback_query_handler(search_callback.filter())
async def group_analyzer_handler(callback: types.CallbackQuery, callback_data: dict):
    await callback.answer(cache_time=60)

    id = callback_data.get('id')

    logging.info(f'Пользователь выбрал группу с id - {id}')

    stats = get_group_stats(id)
    
    await callback.message.answer('Среднее кол-во постов в день: '+str(stats['mean_day_posts'])+
    '\nСреднее кол-во постов в месяц: '+str(stats['mean_month_posts'])+
    '\nСреднее кол-во лайков под постом: '+str(stats['mean_likes'])+
    '\nСреднее кол-во репостов под постом: '+str(stats['mean_reposts'])+
    '\nСреднее кол-во комментариев под постом: '+str(stats['mean_comments'])+
    '\nСреднее кол-во просмотров под постом: '+str(stats['mean_views'])+
    '\nКонверсия просмотров к лайкам: '+str(stats['conv_views_to_likes']))
    await callback.message.edit_reply_markup(reply_markup=None)