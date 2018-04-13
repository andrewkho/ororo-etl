import logging
import sys

import pandas as pd

from extract.yahoo import YahooExtractor

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

logger = logging.getLogger(__name__)


def fetch_forecasts():
    logger.info('Fetching forecasts')
    extractor = YahooExtractor()
    forecast = extractor.get_forecast()
    logger.info("forecast: " + str(forecast))

    # Store forecast in postgres
    # write weather table
    weather_frame = extractor.get_weather_frame(forecast)

    # write forecast table


if __name__ == '__main__':
    fetch_forecasts()
