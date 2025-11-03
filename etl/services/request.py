import os
import requests
from etl.services.settings import *

class Request:

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    def build_API_URL(self, lat, lon):
            return f'https://api.openweathermap.org/data/2.5/weather?lat={str(lat)}&lon={str(lon)}&appid={str(self.API_KEY)}'




request = Request()




