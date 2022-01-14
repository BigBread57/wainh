from loguru import logger
from telegram.ext import CallbackContext


def start_job(context: CallbackContext):
    logger.info('jobs started')
