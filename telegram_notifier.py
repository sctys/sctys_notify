import requests
import json
from notifiers_apikey import TelegramAPI
from notifier_interface import NotifierInterface


class TelegramNotifier(NotifierInterface, TelegramAPI):
    TELEGRAM_ENDPOINT = 'https://api.telegram.org/bot'
    TELEGRAM_SEND = '/sendMessage'

    def __init__(self, project, logger):
        super().__init__(project, logger)
        self.url = self.TELEGRAM_ENDPOINT + self.TELEGRAM_TOKEN + self.TELEGRAM_SEND

    def send_message(self, message, log_only=False):
        message = 'Message from Project: {}\n\n{}'.format(self.project, message)
        try:
            params = {'chat_id': self.CHAT_ID, 'text': message}
            response = json.loads(requests.post(self.url, data=params).content)
        except Exception as e:
            response = {'ok': False, 'error': e}
        return response


