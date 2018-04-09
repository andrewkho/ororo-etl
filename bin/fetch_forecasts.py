import logging
import sys
from logging.handlers import RotatingFileHandler

from extract.yahoo import YahooExtractor

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILENAME = 'log/fetch_forecasts.log'
LOG_MAXBYTES = 20 * 1024 * 1024  # 20 megabytes
LOG_BACKUPCOUNT = 5  # Hold at most 100 megabytes of log file
LOG_LEVEL = logging.INFO  # Only record INFO level or higher in log

logger = logging.getLogger('extract')

logger.setLevel(logging.DEBUG)
filehandler = RotatingFileHandler(filename=LOG_FILENAME, maxBytes=LOG_MAXBYTES, backupCount=LOG_BACKUPCOUNT)
filehandler.setLevel(LOG_LEVEL)
formatter = logging.Formatter(LOG_FORMAT)
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

stdouthandler = logging.StreamHandler(sys.stdout)
stdouthandler.setLevel(logging.DEBUG)
formatter = logging.Formatter(LOG_FORMAT)
stdouthandler.setFormatter(formatter)
logger.addHandler(stdouthandler)


def fetch_forecasts():
    logger.info('Fetching forecasts')
    extractor = YahooExtractor()
    forecast = extractor.get_forecast()
    logger.info("forecast: " + str(forecast))


if __name__ == '__main__':
    fetch_forecasts()
