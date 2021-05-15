import pytest
from src.utils import Utils
import os


class TestUtils:
    def test_get_root_path(self):
        # カレントディレクトリは、作業ディレクトリ
        # これってどうやってテストすればいいんだ？
        assert Utils.get_root_path() == os.path.abspath("./")

    def test_make_dir(self):
        dirpath = "tmp"
        assert os.path.isdir(dirpath) is False
        Utils.make_dir(dirpath)
        assert os.path.isdir(dirpath) is True

    @classmethod
    def teardown_class(cls):
        print("teardown")
        os.rmdir("tmp")
