import logging

logging.getLogger("schedule").setLevel(level=logging.ERROR)
logging.getLogger("root").setLevel(level=logging.ERROR)
logging.getLogger("cronjobs_app").setLevel(level=logging.INFO)
