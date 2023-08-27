from aiogram import types


def get_geo_keyboard(text: str) -> types.ReplyKeyboardMarkup:
    """
    Создание клавиатуры для определения местоположения
    :param text: Текст на кнопке
    :return: ReplyKeyboardMarkup
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text, request_location=True)
    keyboard.add(button)
    return keyboard
