from aiogram import Bot, Dispatcher
from os import getenv
from loguru import logger

logger.info('Loaded dotenv')

class Settings:
    def __init__(self):
        self.is_testing = getenv('TESTING_MODE') == 'TRUE'
        logger.info(f'Is testing = {self.is_testing}')

        self.token = getenv('TEST_BOT_TOKEN') if self.is_testing else getenv('BOT_TOKEN')
        self.admins = getenv('ADMINS').split(',')
        logger.info(f'Admins = {self.admins}')

        logger.info('Loaded .env variables')

        self.bot = Bot(token=self.token)
        logger.info('Created Bot')
        
        self.dp = Dispatcher(self.bot)
        logger.info('Created Dispatcher')