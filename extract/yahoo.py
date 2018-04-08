import json
import logging
from urllib.parse import urlencode
from urllib.request import urlopen

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

            forecasts[k] = forecast['query']['results']

        return forecasts
