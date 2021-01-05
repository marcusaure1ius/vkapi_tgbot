from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

from config import config
import logging

bot = Bot(token=config.TG_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO)

