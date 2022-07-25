from loguru import logger
from os import mkdir, getenv
from dotenv import load_dotenv

load_dotenv()

try: mkdir("Logs")
except FileExistsError: pass

logger.add('Logs/logs.log', format='{time} {level} {message}',\
        level=getenv('LOG_LEVEL'), rotation='1 MB', compression='zip')

logger.info('-'*50)
logger.info('Logging start')