from os import name
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.types import Message

from keyboards.inline.callback_data import search_callback

from group_search import SearchGroup

def getSearchResult(message: Message):

    search_choice = InlineKeyboardMarkup(row_width=1)

    api_search_answer = SearchGroup(message)

    for answer in api_search_answer:
        btn = InlineKeyboardButton(text=answer['group_name'], callback_data=search_callback.new(id=answer['group_id']))
        search_choice.add(btn)

    return search_choice
    