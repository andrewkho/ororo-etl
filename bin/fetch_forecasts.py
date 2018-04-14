import logging
import sys

import pandas as pd

from db import postgres_connector
from extract.yahoo import YahooExtractor

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

logger = logging.getLogger(__name__)


def fetch_forecasts():
    logger.info('Fetching forecasts')
    extractor = YahooExtractor()
    raw_data = extractor.get_forecast()
    logger.info("forecast: " + str(raw_data))

    # Store forecast in postgres
    # write weather table
    logger.info("Writing weather")
    weather_frame = extractor.get_weather_frame(raw_data)
    postgres_connector.store_df(weather_frame, 'yahoo', 'weather')

    logger.info("Writing forecast")
    forecast_frame = extractor.get_forecast_frame(raw_data)
    postgres_connector.store_df(forecast_frame, 'yahoo', 'forecast')

    logger.info("done!")


if __name__ == '__main__':
    fetch_forecasts()
