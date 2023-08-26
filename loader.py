from aiogram import types, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config_data import config
from utils.weather_api.api_call import CurrentWeather

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=MemoryStorage())

Weather_Checker = CurrentWeather()
