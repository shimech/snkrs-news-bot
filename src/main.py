from config import Config
from utils import Utils
from argument_parser import ArgumentParser
from crawler import Crawler
from message import Message
from slack_bot import SlackBot
from logger import Logger


def main():
    arguments = ArgumentParser().arguments

    Utils.make_dir(Config.log_dirpath)
    logger = Logger(filename=Config.log_filename, is_debug=arguments.debug)

    logger.info("Start crawling... (migrate={}, debug={})".format(
        arguments.migrate, arguments.debug))

    news_list, df = Crawler(arguments.migrate, logger).execute()

    if len(news_list) > 0 and not arguments.migrate:
        slack_bot = SlackBot(
            Config.channel, Config.debug_channel, Config.slack_api_token)
        for news in news_list:
            message = Message.make_message(news)
            is_success, status = slack_bot.post_message(
                message,
                is_debug=arguments.debug
            )
            if is_success:
                logger.info(status)
                df.to_csv(Config.database_filename, index=False)
            else:
                logger.error(status)

    logger.info("Stop crawling... (migrate={}, debug={})".format(
        arguments.migrate, arguments.debug))


if __name__ == "__main__":
    main()
