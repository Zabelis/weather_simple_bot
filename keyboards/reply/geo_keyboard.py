from aiogram import types


def get_geo_keyboard(name: str) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(name, request_location=True)
    keyboard.add(button)
    return keyboard
