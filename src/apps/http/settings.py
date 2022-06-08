import logging
from decouple import config
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))
allowed_origins = [
    '*',
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'https://spaceriders.io',
    'http://testnet.spaceriders.io',
    'http://testnet1.spaceriders.io',
    'https://testnet.spaceriders.io'
]

schedule_logger = logging.getLogger('emcache')
schedule_logger.setLevel(level=logging.ERROR)


