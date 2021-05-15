import os
import datetime


class Utils:
    @staticmethod
    def get_root_path():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @staticmethod
    def make_dir(dirpath):
        if not os.path.isdir(dirpath):
            os.makedirs(dirpath)

    @staticmethod
    def get_time_now():
        return datetime.datetime.now()
