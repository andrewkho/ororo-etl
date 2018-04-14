import json
import logging
from urllib.parse import urlencode
from urllib.request import urlopen

import dateutil.parser
import pandas as pd
from pandas.io.json import json_normalize

from extract.extractor import Extractor

logger = logging.getLogger(__name__)

_FORECAST_URL = "https://query.yahooapis.com/v1/public/yql?"
_CITIES = {
    'San Francisco': {'w': 2487956},
    'Vancouver': {'w': 9807},
    'Toronto': {'w': 4118},
    'Edmonton': {'w': 8676},
    'Montreal': {'w': 3534},
    'New York': {'w': 2459115},
    'Sao Paulo': {'w': 455827},
    'Tokyo': {'w': 1118370},
    'Hsinchu': {'w': 2306185},
    'Melbourne': {'w': 1103816},
    'Edinburgh': {'w': 19344},
    'Cairo': {'w': 1521894},
}


class YahooExtractor(Extractor):
    def __init__(self):
        super().__init__()

    def get_weather(self):
        pass

    def _get_yql_url(self, woeid: int, result_format: str = 'json') -> str:
        yql_query = "select * from weather.forecast where woeid=%d" % woeid
        return _FORECAST_URL + urlencode({'q': yql_query}) + "&format=%s" % result_format

    def get_forecast(self):
        forecasts = dict()
        for k, v in _CITIES.items():
            logger.info("Getting forecast for %s" % k)
            yql_url = self._get_yql_url(v['w'])
            logger.debug("yql_url: %s" % yql_url)
            result = urlopen(yql_url)
            data = result.read()
            encoding = result.info().get_content_charset('utf-8')
            forecast = json.loads(data.decode(encoding))
            logger.debug("result: %s" % forecast['query']['results'])

            forecasts[k] = forecast['query']
            forecasts[k]['woe_id'] = v['w']

        return forecasts

    def get_weather_row(self, city: str, forecast: dict) -> pd.DataFrame:
        ts = forecast['created']
        results = forecast['results']['channel']
        loc_id = forecast['woe_id']
        return pd.DataFrame({
            'ts': dateutil.parser.parse(ts, ignoretz=True),  # Already UTC
            'loc_id': int(loc_id),
            'location': str(city),
            'condition_date': dateutil.parser.parse(results['item']['condition']['date'], ignoretz=True),
            'temperature': int(results['item']['condition']['temp']),
            'condition_code': int(results['item']['condition']['code']),
            'condition_text': str(results['item']['condition']['text']),
            'wind_chill': int(results['wind']['chill']),
            'wind_direction': int(results['wind']['direction']),
            'wind_speed': int(results['wind']['speed']),
            'humidity': int(results['atmosphere']['humidity']),
            'pressure': int(float(results['atmosphere']['pressure'])),
            'rising': int(results['atmosphere']['rising']),
            'visibility': float(results['atmosphere']['visibility']),
        }, index=[0])

    def get_weather_frame(self, forecasts: dict) -> pd.DataFrame:
        all_weather = None
        for city, forecast in forecasts.items():
            weather_data = self.get_weather_row(city, forecast)
            if all_weather is None:
                all_weather = weather_data
            else:
                all_weather = all_weather.append(weather_data, ignore_index=True)

        return all_weather

    def get_forecast_rows(self, city: str, forecast: dict) -> pd.DataFrame:
        ts = forecast['created']
        results = forecast['results']['channel']
        loc_id = forecast['woe_id']
        forecast_data = json_normalize(results['item']['forecast'])
        forecast_data['ts'] = dateutil.parser.parse(ts, ignoretz=True)
        forecast_data['loc_id'] = int(loc_id)
        forecast_data['location']: str(city)

        return forecast_data

    def get_forecast_frame(self, forecasts: dict) -> pd.DataFrame:
        all_forecast = None
        for city, forecast in forecasts.items():
            weather_data = self.get_forecast_rows(city, forecast)
            if all_forecast is None:
                all_forecast = weather_data
            else:
                all_forecast = all_forecast.append(weather_data, ignore_index=True)

        return all_forecast
