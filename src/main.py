import os
from dotenv import load_dotenv
from argument_parser import ArgumentParser
from slack_bot import SlackBot


def main():
    load_dotenv()
    argument_parser = ArgumentParser()
    slack_bot = SlackBot(
        os.environ["CHANNEL"], os.environ["TEST_CHANNEL"], os.environ["SLACK_API_TOKEN"])
    slack_bot.post_message("test", is_test=argument_parser.arguments.test)


if __name__ == "__main__":
    main()
