from pprint import pprint

import requests
from config_data import config


class CurrentWeather:
    def __init__(self):
        self.current_url = 'http://api.weatherapi.com/v1/current.json?lang=ru&key={}&q={},{}&aqi=no'
        self.forecast_url = 'http://api.weatherapi.com/v1/forecast.json?lang=ru&key={}&q={},{}&aqi=no&days={}'

    def get_current_weather(self, lat, lon):
        response = requests.get(self.current_url.format(config.WEATHER_API_KEY, lat, lon))
        if response.status_code == 200:
            data = response.json()
            name = data['location']['name']
            current_temp = data['current']['temp_c']
            humidity = data['current']['humidity']
            description = data['current']['condition']['text']
            return name, humidity, description, current_temp

    def get_forecast_weather(self, lat, lon, days):
        response = requests.get(self.forecast_url.format(config.WEATHER_API_KEY, lat, lon, days))
        if response.status_code == 200:
            data = response.json()
            return data

    def get_daily_weather(self, lat, lon, temp_type):
        response = self.get_forecast_weather(lat, lon, 1)
        name = response['location']['name']
        max_temp = response['forecast']['forecastday'][0]['day'][temp_type]
        description = response['current']['condition']['text']
        return name, max_temp, description

    def get_day_weather(self, lat, lon, day):
        response = self.get_forecast_weather(lat, lon, day)
        name = response['location']['name']
        max_temp = response['forecast']['forecastday'][day - 1]['day']['maxtemp_c']
        min_temp = response['forecast']['forecastday'][day - 1]['day']['mintemp_c']
        description = response['forecast']['forecastday'][day - 1]['day']['condition']['text']
        return name, description, max_temp, min_temp
