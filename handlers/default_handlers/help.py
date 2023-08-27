from aiogram.types import Message

from database.SQLite_ORM import User
from loader import dp


@dp.message_handler(commands=["help"])
async def handler_help(message: Message) -> None:
    """
    Сообщение на команду help
    :param message:
    :return: None
    """
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        await message.answer('Вы не зарегистрированы в боте!')
        return
    user = User.get(User.user_id == user_id)
    user.history += '> Запрос помощи\n'
    user.save()
    await message.answer("Доступные команды бота: \n\n"
                         "/low - Минимальная температура \n"
                         "/high - Максимальная температура \n"
                         "/custom - Выбор промежутка времени \n"
                         "/history - История запросов\n"
                         "/custom - Выбор промежутка времени \n"
                         "/my_location - Мое местоположение \n"
                         "/change_location - Изменить местоположение \n"
                         "/delete_user - Удалить аккаунт \n"
                         "/help - Помощь")
