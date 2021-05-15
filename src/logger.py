import logging
from utils import Utils


class Logger:
    def __init__(self, filename, encoding="utf-8", level=logging.INFO, is_debug=False):
        self.is_debug = is_debug
        self.logging = logging
        self.logging.basicConfig(
            filename=filename, encoding=encoding, level=level)

    def info(self, message):
        self.logging.info("[{}] {}".format(Utils.get_time_now(), message))
        self.__print(message)

    def error(self, message):
        self.logging.error("[{}] {}".format(Utils.get_time_now(), message))
        self.__print(message)

    def __print(self, message):
        if self.is_debug:
            print(message)
