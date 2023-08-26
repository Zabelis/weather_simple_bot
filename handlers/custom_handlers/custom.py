from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from database.SQLite_ORM import User
from keyboards.inline.custom_keyboard import get_custom_keyboard
from loader import dp, Weather_Checker


@dp.message_handler(commands=["custom"])
async def handler_custom(message: Message) -> None:
    """
    Сообщение на команду custom
    :param message: Объект сообщения пользователя
    :return: None
    """
    user_id = message.from_user.id

    if User.get_or_none(User.user_id == user_id) is None:
        await message.answer('Вы не зарегистрированы в боте!')
        return
    user = User.get(User.user_id == user_id)
    user.history += '> Запрос промежутка времени команды custom\n'
    user.save()
    custom_keyboard = get_custom_keyboard()
    await message.answer('Выберите промежуток времени для прогноза 👇', reply_markup=custom_keyboard)


@dp.callback_query_handler(Text(equals="today"))
async def handler_today(call: CallbackQuery) -> None:
    """
    Сообщение на команду today
    :param call: Объект сообщения пользователя
    :return: None
    """
    user_id = call.from_user.id

    if User.get_or_none(User.user_id == user_id) is None:
        await call.answer('Вы не зарегистрированы в боте!')
        return
    user = User.get(User.user_id == user_id)
    user.history += '> Запрос прогноза на сегодня\n'
    user.save()

    name, humidity, description, current_temp = Weather_Checker.get_current_weather(user.lat, user.lon)
    await call.message.answer('Прогноз на сегодня:\n\n'
                              'Место: {}\n'
                              'Погода: {}\n'
                              'Температура: {}°C\n'
                              'Влажность: {}%\n'.format(name, description, current_temp, humidity))
    await call.answer()


@dp.callback_query_handler(Text(equals="tomorrow"))
async def handler_tomorrow(call: CallbackQuery) -> None:
    """
    Сообщение на CallbackQuery tomorrow
    :param call: Объект сообщения пользователя
    :return: None
    """
    user_id = call.from_user.id

    if User.get_or_none(User.user_id == user_id) is None:
        await call.answer('Вы не зарегистрированы в боте!')
        return
    user = User.get(User.user_id == user_id)
    user.history += '> Запрос прогноза на завтра\n'
    user.save()

    name, description, max_temp, min_temp = Weather_Checker.get_day_weather(user.lat, user.lon, 2)
    await call.message.answer('Прогноз на завтра:\n\n'
                              'Место: {}\n'
                              'Максимальная температура: {}°C\n'
                              'Минимальная температура: {}°C\n'
                              'Погода: {}\n'.format(name, max_temp, min_temp, description))
    await call.answer()


@dp.callback_query_handler(Text(equals="after_tomorrow"))
async def handler_after_tomorrow(call: CallbackQuery) -> None:
    """
    Сообщение на CallbackQuery after_tomorrow
    :param call: Объект сообщения пользователя
    :return: None
    """
    user_id = call.from_user.id

    if User.get_or_none(User.user_id == user_id) is None:
        await call.answer('Вы не зарегистрированы в боте!')
        return
    user = User.get(User.user_id == user_id)
    user.history += '> Запрос прогноза на послезавтра\n'
    user.save()

    name, description, max_temp, min_temp = Weather_Checker.get_day_weather(user.lat, user.lon, 3)
    await call.message.answer('Прогноз на послезавтра:\n\n'
                              'Место: {}\n'
                              'Максимальная температура: {}°C\n'
                              'Минимальная температура: {}°C\n'
                              'Погода: {}\n'.format(name, max_temp, min_temp, description))
    await call.answer()
