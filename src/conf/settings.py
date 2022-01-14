import sys
from pathlib import Path

import environ
from loguru import logger

ROOT_DIR = Path(__file__).parents[2]
BASE_DIR = ROOT_DIR / 'src'

env = environ.Env()

READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE and (ROOT_DIR / '.env').exists():
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / '.env'))

logger.add(sys.stderr, format='{time} {level} {message}')

BOT_TOKEN = env.str('BOT_TOKEN', default='')
JOB_TIME = env.int('JOB_TIME', default=60)  # Time to delete bot messages in seconds, default one hour
