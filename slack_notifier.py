from notifiers_apikey import SlackAPI
from notifier_interface import NotifierInterface
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackNotifier(NotifierInterface, SlackAPI):

    def __init__(self, project, logger):
        super().__init__(project, logger)

    def send_message(self, message):
        try:
            sc = WebClient(self.SLACK_BOT_TOKEN)
            response = sc.chat_postMessage(channel=self.SLACK_CHANNEL[self.project], text=message)
        except SlackApiError as e:
            response = {'ok': False, 'error': e.response['error']}
        return response


