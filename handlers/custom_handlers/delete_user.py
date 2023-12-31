from aiogram.types import Message

from database.SQLite_ORM import User
from loader import dp, log


@dp.message_handler(commands=["delete_user"])
async def handler_delete_user(message: Message) -> None:
    """
    Сообщение на команду delete_user
    :param message: Объект сообщения пользователя
    :return: None
    """
    user_id = message.from_user.id
    try:
        if User.get_or_none(User.user_id == user_id) is None:
            await message.answer('Вы не зарегистрированы в боте!')
            return

        User.get(User.user_id == user_id).delete_instance()
        await message.answer('Аккаунт удален!')
    except Exception as e:
        log.error('Возникла ошибка:', e)
        await message.answer('Внимание! Произошла ошибка! Нужно связаться с разработчиком')
