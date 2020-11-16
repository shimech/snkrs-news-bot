import os
from dotenv import load_dotenv
from argument_parser import ArgumentParser
from crawler import Crawler
from message import Message
from slack_bot import SlackBot


def main():
    load_dotenv()
    argument_parser = ArgumentParser()

    mode = "stock" if argument_parser.arguments.stock else "timeline"
    news_list = Crawler.run(mode=mode)

    if news_list is not None:
        slack_bot = SlackBot(
            os.environ["CHANNEL"], os.environ["TEST_CHANNEL"], os.environ["SLACK_API_TOKEN"])
        for news in news_list:
            message = Message.make_message(news, mode)
            slack_bot.post_message(
                message,
                is_test=argument_parser.arguments.test
            )


if __name__ == "__main__":
    main()
