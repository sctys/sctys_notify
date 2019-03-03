from apikey import SlackAPI
from setting import SlackSetting
from slackclient import SlackClient
import logging
import os
import time


class SlackNotifier(SlackAPI, SlackSetting):

    def __init__(self):
        self.logger = None
        self.set_logger()

    def set_logger(self):
        logger_file = os.path.join(self.SLACK_LOGGER_PATH, self.SLACK_LOGGER_FILE)
        logging.basicConfig(filename=logger_file, level=getattr(logging, self.SLACK_LOGGER_LEVEL),
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def send_message(self, message):
        sc = SlackClient(self.SLACK_BOT_TOKEN)
        response = sc.api_call('chat.postMessage', channel=self.SLACK_CHANNEL, text=message)
        return response

    def retry(self, func, *params):
        count = 0
        run_success = False
        while count < self.SLACK_NUM_RETRY and not run_success:
            try:
                response = func(params)
                if response is None or not response['ok']:
                    self.logger.error('Unable to send Slack message. {}'.format(response['error']))
                    time.sleep(self.SLACK_SLEEP)
                    count += 1
                else:
                    run_success = True
            except Exception as e:
                self.logger.error('Error in sending Slack message. {}'.format(e))
                time.sleep(self.SLACK_SLEEP)
                count += 1


def test():
    sn = SlackNotifier()
    sn.retry(sn.send_message, 'test')


if __name__ == '__main__':
    test()

