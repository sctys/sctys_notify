import os

class SlackSetting(object):
    SLACK_NUM_RETRY = 5
    SLACK_SLEEP = 10
    SLACK_LOGGER_PATH = os.environ['SCTYS_PROJECT'] + '/Log/log_sctys_notify/'
    SLACK_LOGGER_FILE = 'slack_notifier.log'
    SLACK_LOGGER_LEVEL = 'DEBUG'


class TelegramSetting(object):
    TELEGRAM_NUM_RETRY = 5
    TELEGRAM_SLEEP = 10
    TELEGRAM_LOGGER_PATH = os.environ['SCTYS_PROJECT'] + '/Log/log_sctys_notify/'
    TELEGRAM_LOGGER_FILE = 'telegram_notifier.log'
    TELEGRAM_LOGGER_LEVEL = 'DEBUG'
    TELEGRAM_ENDPOINT = 'https://api.telegram.org/bot'
    TELEGRAM_SEND = '/sendMessage'