from core.shared.ports import LoggingPort
from logging import Logger
import logging
import sys
from decouple import config
from pythonjsonlogger import jsonlogger

class LoggingAdapter(LoggingPort):

    def __init__(self, logger) -> None:
        self.logger: Logger = logger

    async def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    async def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)


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