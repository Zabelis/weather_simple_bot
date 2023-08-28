from aiogram.types import Message

from database.SQLite_ORM import User
from loader import dp, log


@dp.message_handler()
async def unknown_handler(message: Message) -> None:
    user_id = message.from_user.id

    try:
        if User.get_or_none(User.user_id == user_id) is None:
            await message.answer('Вы не зарегистрированы в боте!')
            return

        user = User.get(User.user_id == user_id)
        user.history += '> Неизвестная команда\n'
        user.save()
        await message.answer("Команда не распознана")
    except Exception as e:
        log.error('Возникла ошибка:', e)
        await message.answer('Внимание! Произошла ошибка! Нужно связаться с разработчиком')
