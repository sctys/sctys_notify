import requests
import json
from apikey import TelegramAPI
from setting import TelegramSetting
from utilities import retry, set_logger


class TelegramNotifier(TelegramAPI, TelegramSetting):

    def __init__(self):
        self.url = self.TELEGRAM_ENDPOINT + self.TELEGRAM_TOKEN + self.TELEGRAM_SEND
        self.logger = None
        self.set_logger()

    def set_logger(self):
        self.logger = set_logger(self.TELEGRAM_LOGGER_PATH, self.TELEGRAM_LOGGER_FILE, self.TELEGRAM_LOGGER_LEVEL,
                                 __name__)

    def _send_message(self, message):
        try:
            params = {'chat_id': self.CHAT_ID, 'text': message}
            response = json.loads(requests.post(self.url, data=params).content)
        except Exception as e:
            response = {'ok': False, 'error': e}
        return response

    @staticmethod
    def _message_checker(response):
        if not response['ok']:
            result = {'status': False, 'message': response['error']}
        else:
            result = {'status': True, 'message': None}
        return result

    def send_message(self, message):
        retry(self._send_message, message, checker=self._message_checker, num_retry=self.TELEGRAM_NUM_RETRY,
              sleep_time=self.TELEGRAM_SLEEP, logger=self.logger)


def test():
    tn = TelegramNotifier()
    tn.send_message('test')


if __name__ == '__main__':
    test()

