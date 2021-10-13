import os
import sys
sys.path.append(os.environ['SCTYS_PROJECT'] + '/sctys_utilities')
from utilities_functions import retry_wrapper


class NotifierInterface(object):

    NUM_RETRY = 5
    TIME_SLEEP = 10

    def __init__(self, project, logger):
        self.project = project
        self.logger = logger

    def set_num_retry(self, num_retry):
        self.NUM_RETRY = num_retry

    def set_time_sleep(self, time_sleep):
        self.TIME_SLEEP = time_sleep

    @ staticmethod
    def message_checker(response):
        if not response['ok']:
            result = {'status': False, 'terminate': False, 'message': response['error']}
        else:
            result = {'status': True, 'terminate': True, 'message': None}
        return result

    def send_message(self, message):
        raise NotImplementedError

    def retry_send_message(self, message):
        return retry_wrapper(
            self.send_message, self.message_checker, self.NUM_RETRY, self.TIME_SLEEP, self.logger)(message)

