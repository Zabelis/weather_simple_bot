from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp


@dp.message_handler(Text(equals='Привет'))
@dp.message_handler(commands=["hello_world"])
async def handler_hello_world(message: Message) -> None:
    await message.answer('Привет!')
