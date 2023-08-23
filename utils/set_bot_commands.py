from aiogram import types, Dispatcher


async def set_default_commands(dp: Dispatcher) -> None:
    """
    Установка команд бота
    :param dp: Диспатчер бота
    :return: None
    """
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('hello_world', 'Приветствие'),
            types.BotCommand('low', 'Минимальная температура'),
            types.BotCommand('low', 'Минимальная температура'),
            types.BotCommand('high', 'Максимальная температура'),
            types.BotCommand('custom', 'Выбор промежутка времени'),
            types.BotCommand('history', 'История запросов'),
            types.BotCommand('help', 'Помощь'),
            types.BotCommand('change_location', 'Изменить местоположение'),
            types.BotCommand('my_location', 'Мой местоположение'),
        ]
    )
