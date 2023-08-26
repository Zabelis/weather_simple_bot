from aiogram.types import Message

from database.SQLite_ORM import User
from loader import dp, Weather_Checker


@dp.message_handler(commands=["low"])
async def handler_min_temperature(message: Message) -> None:
    """
    Сообщение на команду low
    :param message: Объект сообщения пользователя
    :return: None
    """
    user_id = message.from_user.id

    if User.get_or_none(User.user_id == user_id) is None:
        await message.answer('Вы не зарегистрированы в боте!')
        return
    user = User.get(User.user_id == user_id)
    name, min_temp, description = Weather_Checker.get_daily_weather(user.lat, user.lon, 'mintemp_c')
    user.history += '> Запрос минимальной температуры для места: {}\n'.format(name)
    user.save()
    await message.answer(f'Место: {name}\n'
                         f'Погода: {description}\n'
                         f'Минимальная температура: {min_temp}°C')
