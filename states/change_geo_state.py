from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeGeoState(StatesGroup):
    """
    Класс состояния: ожидание геолокации для ее изменения
    """
    change_location = State()
