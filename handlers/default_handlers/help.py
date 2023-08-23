from aiogram.types import Message

from loader import dp


@dp.message_handler(commands=["help"])
async def handle_help(message: Message) -> None:
    await message.answer("Доступные команды бота: \n\n"
                         "/low - Минимальная температура \n"
                         "/high - Максимальная температура \n"
                         "/custom - Выбор промежутка времени \n"
                         "/history - История запросов\n"
                         "/custom - Выбор промежутка времени \n"
                         "/my_location - Мое местоположение \n"
                         "/change_location - Изменить местоположение \n"
                         "/help - Помощь")
