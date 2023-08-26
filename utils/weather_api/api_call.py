from pprint import pprint

import requests
from config_data import config


class CurrentWeather:
    """
    Класс для получения прогноза погоды
    """
    def __init__(self):
        """
        Инициализация ссылок для получения текущей погоды и погоды на будущие дни
        """
        self.current_url = 'http://api.weatherapi.com/v1/current.json?lang=ru&key={}&q={},{}&aqi=no'
        self.forecast_url = 'http://api.weatherapi.com/v1/forecast.json?lang=ru&key={}&q={},{}&aqi=no&days={}'

    def get_current_weather(self, lat, lon):
        """
        Получение текущей погоды
        :param lat: долгота местоположения
        :param lon: широта местоположения
        :return:
        """
        response = requests.get(self.current_url.format(config.WEATHER_API_KEY, lat, lon))
        if response.status_code == 200:
            data = response.json()
            name = data['location']['name']
            current_temp = data['current']['temp_c']
            humidity = data['current']['humidity']
            description = data['current']['condition']['text']
            return name, humidity, description, current_temp

    def get_forecast_weather(self, lat, lon, days):
        """
        Получение прогноза погоды на будущие дни
        :param lat: Долгота
        :param lon: Широта
        :param days: Количество дней
        :return:
        """
        response = requests.get(self.forecast_url.format(config.WEATHER_API_KEY, lat, lon, days))
        if response.status_code == 200:
            data = response.json()
            return data

    def get_daily_weather(self, lat, lon, temp_type):
        """
        Прогноз погоды на сегодня
        :param lat: Долгота
        :param lon: Широта
        :param temp_type: Тип температуры (макс/мин)
        :return:
        """
        response = self.get_forecast_weather(lat, lon, 1)
        name = response['location']['name']
        temp = response['forecast']['forecastday'][0]['day'][temp_type]
        description = response['current']['condition']['text']
        return name, temp, description

    def get_day_weather(self, lat, lon, day):
        """
        Прогноз погоды на день
        :param lat: Долгота
        :param lon: Широта
        :param day: Кол-во дней
        :return:
        """
        response = self.get_forecast_weather(lat, lon, day)
        name = response['location']['name']
        max_temp = response['forecast']['forecastday'][day - 1]['day']['maxtemp_c']
        min_temp = response['forecast']['forecastday'][day - 1]['day']['mintemp_c']
        description = response['forecast']['forecastday'][day - 1]['day']['condition']['text']
        return name, description, max_temp, min_temp
