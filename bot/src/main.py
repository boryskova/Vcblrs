import logging

from aiogram import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from bot_app.app import dp


logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
