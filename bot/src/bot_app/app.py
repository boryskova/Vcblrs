from aiogram import Bot, Dispatcher

from .local_settings import API_KEY


bot = Bot(token=API_KEY)
dp = Dispatcher(bot)
