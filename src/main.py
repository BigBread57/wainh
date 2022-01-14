from telegram.ext import Updater

from conf.settings import BOT_TOKEN, JOB_TIME, logger
from handlers import start_handler
from jobs import start_job


def main():
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    job_queue = updater.job_queue

    dispatcher.add_handler(start_handler)

    job_queue.run_repeating(start_job, JOB_TIME)

    # Start the Bot
    updater.start_polling()
    logger.info('bot started')

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
