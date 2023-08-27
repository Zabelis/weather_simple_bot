import logging

from aiogram import types, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config_data import config
from utils.weather_api.api_call import CurrentWeather

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=MemoryStorage())

Weather_Checker = CurrentWeather()

log = logging.getLogger(__name__)
fileHandler = logging.FileHandler(filename='errors.log', encoding='utf-8')
logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s', handlers=[fileHandler],
                    level=logging.INFO)
