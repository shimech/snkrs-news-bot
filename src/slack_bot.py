from slacker import Slacker
from utils import Utils


class SlackBot:
    def __init__(self, channel, debug_channel, slack_api_token):
        self.slacker = Slacker(slack_api_token)
        self.channel = channel
        self.debug_channel = debug_channel

    def post_message(self, message, is_debug=False):
        channel = self.debug_channel if is_debug else self.channel
        try:
            self.slacker.chat.post_message(channel, message)
            return True, "post message to {}".format(channel)
        except:
            return False, "FAIL to post message to {}".format(channel)
