from aiogram import types


def get_custom_keyboard() -> types.InlineKeyboardMarkup:
    """
    Создание клавиатуры для выбора прогноза в определенном промежутке времени
    :return: Клавиатура InlineKeyboardMarkup
    """
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Погода сейчас", callback_data="today")
    btn2 = types.InlineKeyboardButton(text="Прогноз на завтра", callback_data="tomorrow")
    btn3 = types.InlineKeyboardButton(text="Прогноз на послезавтра", callback_data="after_tomorrow")
    keyboard.add(btn1, btn2, btn3)
    return keyboard
