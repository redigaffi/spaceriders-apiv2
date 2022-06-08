import logging
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))

schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.ERROR)

logging.getLogger('emcache').setLevel(level=logging.ERROR)