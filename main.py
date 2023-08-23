import logging

from aiogram import Dispatcher

from database.SQLite_ORM import create_models
from handlers import dp
from utils.set_bot_commands import set_default_commands
from aiogram import executor


async def on_startup(dp: Dispatcher):
    await set_default_commands(dp)
    print("Бот запущен!")


if __name__ == '__main__':
    create_models()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
