import logging
from decouple import config

allowed_origins = [
    '*',
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'https://spaceriders.io',
    'http://testnet.spaceriders.io',
    'https://testnet.spaceriders.io'
]

schedule_logger = logging.getLogger('emcache')
schedule_logger.setLevel(level=logging.ERROR)
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# logging.basicConfig(encoding='utf-8',
#                     level=config('LOG_LEVEL'),
#                     format="%(asctime)s %(levelname)s %(message)s")


