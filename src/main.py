import os
from dotenv import load_dotenv
from argument_parser import ArgumentParser
from utils import Utils
from crawler import Crawler
from message import Message
from slack_bot import SlackBot


def main():
    load_dotenv()
    argument_parser = ArgumentParser()

    mode = __select_mode(argument_parser.arguments)
    Utils.print_log("start bot (mode={})".format(mode))

    news_list = Crawler.run(
        mode=mode, is_migrate=argument_parser.arguments.migrate)

    if len(news_list) > 0 and not argument_parser.arguments.migrate:
        slack_bot = SlackBot(
            os.environ["CHANNEL"], os.environ["TEST_CHANNEL"], os.environ["SLACK_API_TOKEN"])
        for news in news_list:
            message = Message.make_message(news, mode)
            slack_bot.post_message(
                message,
                is_test=argument_parser.arguments.test
            )

    Utils.print_log("stop bot (mode={})".format(mode))


def __select_mode(arguments):
    if arguments.stock:
        return "stock"
    else:
        return "timeline"


if __name__ == "__main__":
    main()
