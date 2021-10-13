import os
import sys
import inspect
sys.path.append(os.environ['SCTYS_PROJECT'] + '/sctys_utilities')
from utilities_functions import set_logger
from slack_notifier import SlackNotifier
from telegram_notifier import TelegramNotifier


def test_slack_send_message():
    project = 'sctys_notify'
    logger_path = os.environ['SCTYS_PROJECT'] + '/Log/log_sctys_notify'
    logger_file_name = inspect.currentframe().f_code.co_name + '.log'
    logger_name = inspect.currentframe().f_code.co_name
    logger_level = 'DEBUG'
    logger = set_logger(logger_path, logger_file_name, logger_level, logger_name)
    sn = SlackNotifier(project, logger)
    sn.retry_send_message('testing')


def test_telegram_send_message():
    project = 'sctys_notify'
    logger_path = os.environ['SCTYS_PROJECT'] + '/Log/log_sctys_notify'
    logger_file_name = inspect.currentframe().f_code.co_name + '.log'
    logger_name = inspect.currentframe().f_code.co_name
    logger_level = 'DEBUG'
    logger = set_logger(logger_path, logger_file_name, logger_level, logger_name)
    tn = TelegramNotifier(project, logger)
    tn.retry_send_message('testing')


if __name__ == '__main__':
    test_slack_send_message()
    test_telegram_send_message()