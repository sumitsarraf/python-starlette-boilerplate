import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('Logs/mystarlette_app')

handler = RotatingFileHandler('Logs/mystarlette_app.log', maxBytes=3000000,backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
handler.close()

def get_logger() :
    return logger