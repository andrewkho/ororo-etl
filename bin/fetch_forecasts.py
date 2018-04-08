import logging
import sys

from extract.yahoo import YahooExtractor

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=log_format)

logger = logging.getLogger(__name__)


def fetch_forecasts():
    logger.info('Fetching forecasts')
    extractor = YahooExtractor()
    forecast = extractor.get_forecast()
    logger.info("forecast: " + str(forecast))


if __name__ == '__main__':
    fetch_forecasts()
