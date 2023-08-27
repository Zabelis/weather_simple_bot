from aiogram.types import Message

from database.SQLite_ORM import User
from loader import dp, log


@dp.message_handler(commands=["history"])
async def handler_history(message: Message) -> None:
    """
    Сообщение на команду history
    :param message: Объект сообщения пользователя
    :return: None
    """
    user_id = message.from_user.id

    try:
        if User.get_or_none(User.user_id == user_id) is None:
            await message.answer('Вы не зарегистрированы в боте!')
            return

        user = User.get(User.user_id == user_id)
        history = user.history
        user.history += '> Запрос истории запросов\n'
        user.save()
        if history:
            await message.answer(history)
        else:
            await message.answer('История запросов пуста')
    except Exception as e:
        log.error('Возникла ошибка:', e)
        await message.answer('Внимание! Произошла ошибка! Нужно связаться с разработчиком')
