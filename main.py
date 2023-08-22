import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types


BOT_TOKEN = os.environ.get('BOT_TOKEN')

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(filename='logging_info.log', encoding='utf-8')
logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', handlers=[fileHandler],
                    level=logging.INFO)
date_format = "%d.%m.%Y %H:%M"


async def main():
    """Bot initialization main function."""
    bot = Bot(token=BOT_TOKEN,
              parse_mode=types.ParseMode.HTML)  # создание бота и его токен

    dp = Dispatcher(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
