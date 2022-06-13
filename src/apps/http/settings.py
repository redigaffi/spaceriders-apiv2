import logging


allowed_origins = [
    '*',
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'https://spaceriders.io',
    'http://testnet.spaceriders.io',
    'http://testnet1.spaceriders.io',
    'https://testnet.spaceriders.io'
]

logging.getLogger('root').setLevel(level=logging.ERROR)


