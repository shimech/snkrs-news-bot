import os
from dotenv import load_dotenv
from argument_parser import ArgumentParser
from message import Message
from slack_bot import SlackBot


def main():
    load_dotenv()
    argument_parser = ArgumentParser()

    news_list = [{
        "name": "name",
        "url": "url",
        "is_snkrs_pass": False
    }]

    if news_list is not None:
        slack_bot = SlackBot(
            os.environ["CHANNEL"], os.environ["TEST_CHANNEL"], os.environ["SLACK_API_TOKEN"])
        for news in news_list:
            message = Message.make_message(
                news.get("name"), news.get("url"), news.get("is_snkrs_pass"))
            slack_bot.post_message(
                message,
                is_test=argument_parser.arguments.test
            )


if __name__ == "__main__":
    main()
