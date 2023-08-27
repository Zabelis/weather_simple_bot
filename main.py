import logging

from aiogram import Dispatcher

from database.SQLite_ORM import create_models
from handlers import dp
from loader import log
from utils.set_bot_commands import set_default_commands
from aiogram import executor


async def on_startup(dp: Dispatcher) -> None:
    """
    Функция запускаемая при запуске бота
    :param dp:
    :return: None
    """
    await set_default_commands(dp)
    log.info("Бот запущен!")


if __name__ == '__main__':
    create_models()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
