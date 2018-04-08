import requests

from extract.extractor import Extractor

_FORECAST_URL = 'http://ES_search_demo.com/document/record/_search?pretty=true'
_CITIES = {
    'San Francisco': {'id': 5391959, 'name': 'San Francisco', 'country': 'US',
                      'coord': {'lon': -122.419418, 'lat': 37.774929}},
    'Vancouver': {'id': 6173331, 'name': 'Vancouver', 'country': 'CA', 'coord': {'lon': -123.119339, 'lat': 49.24966}},
    'Toronto': {'id': 6167865, 'name': 'Toronto', 'country': 'CA', 'coord': {'lon': -79.416298, 'lat': 43.700111}},
    'Edmonton': {'id': 5946768, 'name': 'Edmonton', 'country': 'CA', 'coord': {'lon': -113.468712, 'lat': 53.55014}},
    'New York': {'id': 5128581, 'name': 'New York', 'country': 'US', 'coord': {'lon': -74.005966, 'lat': 40.714272}},
    'Sao Paulo': {'id': 3448439, 'name': 'Sao Paulo', 'country': 'BR', 'coord': {'lon': -46.636108, 'lat': -23.547501}},
    'Tokyo': {'id': 1850147, 'name': 'Tokyo', 'country': 'JP', 'coord': {'lon': 139.691711, 'lat': 35.689499}},
    'Hsinchu': {'id': 1675151, 'name': 'Hsinchu', 'country': 'TW', 'coord': {'lon': 120.968613, 'lat': 24.80361}},
    'Melbourne': {'id': 2158177, 'name': 'Melbourne', 'country': 'AU', 'coord': {'lon': 144.963318, 'lat': -37.813999}},
}


class OpenWeatherExtractor(Extractor):
    def __init__(self):
        super().__init__()
        pass

    def get_weather(self):
        pass

    def get_forecast(self):
        data = '''{
          "query": {
            "bool": {
              "must": [
                {
                  "text": {
                    "record.document": "SOME_JOURNAL"
                  }
                },
                {
                  "text": {
                    "record.articleTitle": "farmers"
                  }
                }
              ],
              "must_not": [],
              "should": []
            }
          },
          "from": 0,
          "size": 50,
          "sort": [],
          "facets": {}
        }'''
        response = requests.post(_FORECAST_URL, data=data)
