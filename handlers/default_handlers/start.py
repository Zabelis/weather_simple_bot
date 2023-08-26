from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from peewee import IntegrityError

from database.SQLite_ORM import User
from keyboards.reply.geo_keyboard import get_geo_keyboard
from loader import dp
from states.geo_state import GeoState


@dp.message_handler(commands=["start"])
async def handler_start(message: Message, state: FSMContext) -> None:
    """
    Сообщение на команду start
    :param message:
    :param state:
    :return: None
    """
    user_id = message.from_user.id

    if User.get_or_none(User.user_id == user_id):
        await message.answer('Вы уже зарегистрированы в боте!')
        return

    geo_button = get_geo_keyboard('Определить местоположение')
    await message.answer("Добро пожаловать в бот погоды! "
                         "Для полноценной работы необходимо определить вашу геопозицию, "
                         "поэтому нажмите на кнопку 'Определить местоположение'", reply_markup=geo_button)
    await state.set_state(GeoState.current_location)


@dp.message_handler(state=GeoState.current_location, content_types=['location'])
async def save_geo(message: Message, state: FSMContext) -> None:
    """
    Сохранение геопозиции
    :param message:
    :param state:
    :return:
    """
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    lat = message.location.latitude
    lon = message.location.longitude
    try:
        User.create(user_id=user_id, username=username, first_name=first_name, last_name=last_name, lat=lat, lon=lon,
                    history='> Создание аккаунта\n')
        await state.finish()
        await message.answer('Ваша геопозиция сохранена!\n'
                             'Для ознакомления с возможностями бота используйте команду /help',
                             reply_markup=types.ReplyKeyboardRemove())
    except Exception as e:
        print('Возникла ошибка:', e)
        await message.answer('Внимание! При сохранении вашего аккаунта возникла ошибка! '
                             'Попробуйте отправить геопозицию еще раз!')
