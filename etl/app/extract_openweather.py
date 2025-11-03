import sys
from pathlib import Path
import json
# from etl.services.minio_client import MinioClient
from etl.services.request import request
import requests
from datetime import datetime
from etl.services.minio_client import MinioClient

class ExtractOpenWeather:

    request = request

    def test(self):
        # first value - lat, second - lon
        cities = {
            'Moscow': (55.7558, 37.6173)
        }

        city = 'Moscow'
        lat, lon = cities[city]
        url_for_moscow = self.request.build_API_URL(lat, lon)
        print(url_for_moscow)

        request = requests.get(url_for_moscow)

        json_data = request.json()
        print(json_data)
        json_text = json.dumps(json_data, ensure_ascii=False, separators=(',', ':'))
        print(json_text)
        body_bytes = json_text.encode('utf-8')
        date_current = datetime.utcnow()
        object_name = (f'raw/openweather/city='
                       f'{city.lower()}/'
                       f'{datetime.strftime(date_current, "%Y")}/'
                       f'{datetime.strftime(date_current, "%m")}/'
                       f'{datetime.strftime(date_current, "%d")}/'
                       f'{datetime.strftime(date_current, "%H")}-'
                       f'{datetime.strftime(date_current, "%M")}.json')

        print(object_name)

        minio = MinioClient()
        minio.fun()
        res = minio.build_put_object(object_name, body_bytes)
        print(f'res : {res}')

extract = ExtractOpenWeather()