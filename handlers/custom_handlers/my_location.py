import logging

from aiogram.types import Message

from database.SQLite_ORM import User
from loader import dp, log


@dp.message_handler(commands=["my_location"])
async def handler_my_location(message: Message) -> None:
    """
    Сообщение на команду my_location
    :param message: Объект сообщения пользователя
    :return: None
    """
    user_id = message.from_user.id

    try:
        if User.get_or_none(User.user_id == user_id) is None:
            await message.answer('Вы не зарегистрированы в боте!')
            return

        user = User.get(User.user_id == user_id)
        user.history += '> Запрос местоположения\n'
        user.save()
        await message.answer("Ваша геопозиция: \n\n"
                             "Долгота: {}\n"
                             "Широта: {}".format(user.lat, user.lon))
    except Exception as e:
        log.error('Возникла ошибка:', e)
        await message.answer('Внимание! Произошла ошибка! Нужно связаться с разработчиком')
