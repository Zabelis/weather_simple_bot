from aiogram.dispatcher.filters.state import StatesGroup, State


class GeoState(StatesGroup):
    """
    Класс состояния: ожидание геолокации
    """
    current_location = State()
