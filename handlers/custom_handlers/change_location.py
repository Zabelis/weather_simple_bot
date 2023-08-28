from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from database.SQLite_ORM import User
from keyboards.reply.geo_keyboard import get_geo_keyboard
from loader import dp, log
from states.change_geo_state import ChangeGeoState


@dp.message_handler(commands=["change_location"])
async def handler_change_location(message: Message, state: FSMContext) -> None:
    """
    Сообщение на команду change_location
    :param state: Состояние пользователя
    :param message: Объект сообщения пользователя
    :return: None
    """
    user_id = message.from_user.id

    try:
        if User.get_or_none(User.user_id == user_id) is None:
            await message.answer('Вы не зарегистрированы в боте!')
            return

        await state.set_state(ChangeGeoState.change_location)
        geo_button = get_geo_keyboard('Изменить местоположение')
        await message.answer("Поделитесь вашей геопозицией, чтобы изменить местоположение",
                             reply_markup=geo_button)
    except Exception as e:
        log.error('Возникла ошибка:', e)
        await message.answer('Внимание! Произошла ошибка! Нужно связаться с разработчиком')


@dp.message_handler(state=ChangeGeoState.change_location, content_types=['location'])
async def save_geo(message: Message, state: FSMContext) -> None:
    """
    Сохранение новой геопозиции
    :param message:
    :param state:
    :return: None
    """

    try:
        user = User.get(User.user_id == message.from_user.id)
        user.lat = message.location.latitude
        user.lon = message.location.longitude
        user.history += '> Изменение местоположения на {} {}\n'.format(user.lat,
                                                                       user.lon)
        user.save()
        await state.finish()
        await message.answer('Ваша геопозиция изменена!\n',
                             reply_markup=types.ReplyKeyboardRemove())
    except Exception as e:
        print('Возникла ошибка:', e)
        await message.answer('Внимание! При сохранении вашего аккаунта возникла ошибка! '
                             'Попробуйте отправить геопозицию еще раз!')
