import logging
import sys
from decouple import config
from pythonjsonlogger import jsonlogger

def get_logger(name: str):
    logging.basicConfig(level=config('LOG_LEVEL'))
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level=logging.NOTSET)
        #logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

        handler.setFormatter(jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s'))
        logger.addHandler(handler)
        logger.propagate = 0

    return logger

schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.ERROR)