from notifiers_apikey import SlackAPI
from notifier_interface import NotifierInterface
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackNotifier(NotifierInterface, SlackAPI):

    def __init__(self, project, logger):
        super().__init__(project, logger)

    def send_message(self, message, log_only=False):
        if log_only and self.project + '_log_only' in self.SLACK_CHANNEL:
            project = self.project + '_log_only'
        else:
            project = self.project
        try:
            sc = WebClient(self.SLACK_BOT_TOKEN)
            response = sc.chat_postMessage(channel=self.SLACK_CHANNEL[project], text=message)
        except SlackApiError as e:
            response = {'ok': False, 'error': e.response['error']}
        return response


