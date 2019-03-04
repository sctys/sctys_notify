from apikey import SlackAPI
from setting import SlackSetting
from slackclient import SlackClient
from utilities import retry, set_logger


class SlackNotifier(SlackAPI, SlackSetting):

    def __init__(self):
        self.logger = None
        self.set_logger()

    def set_logger(self):
        self.logger = set_logger(self.SLACK_LOGGER_PATH, self.SLACK_LOGGER_FILE, self.SLACK_LOGGER_LEVEL, __name__)

    def _send_message(self, message):
        try:
            sc = SlackClient(self.SLACK_BOT_TOKEN)
            response = sc.api_call('chat.postMessage', channel=self.SLACK_CHANNEL, text=message)
        except Exception as e:
            response = {'ok': False, 'error': e}
        return response

    @ staticmethod
    def _message_checker(response):
        if not response['ok']:
            result = {'status': False, 'message': response['error']}
        else:
            result = {'status': True, 'message': None}
        return result

    def send_message(self, message):
        retry(self._send_message, message, checker=self._message_checker, num_retry=self.SLACK_NUM_RETRY,
              sleep_time=self.SLACK_SLEEP, logger=self.logger)


def test():
    sn = SlackNotifier()
    sn.send_message('test')


if __name__ == '__main__':
    test()

