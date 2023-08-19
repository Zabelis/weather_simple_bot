import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types

from weather_module.weather_handlers import register_weather_handlers

BOT_TOKEN = os.environ.get('BOT_TOKEN')

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(filename='logging_info.log', encoding='utf-8')
logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', handlers=[fileHandler],
                    level=logging.INFO)
date_format = "%d.%m.%Y %H:%M"


async def register_handlers(dp: Dispatcher):
    """Registration all handlers before processing update."""
    register_weather_handlers(dp)


async def main():
    """Bot initialization main function."""
    bot = Bot(token=BOT_TOKEN,
              parse_mode=types.ParseMode.HTML)  # создание бота и его токен

    dp = Dispatcher(bot)

    await register_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
