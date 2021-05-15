import os
from dotenv import load_dotenv
from utils import Utils
load_dotenv()


class Config:
    # 環境変数
    timeline_url = os.getenv("URL")
    slack_api_token = os.getenv("SLACK_API_TOKEN")
    channel = os.getenv("CHANNEL")
    debug_channel = os.getenv("DEBUG_CHANNEL")

    # PATH
    root_path = Utils.get_root_path()
    log_dirpath = os.path.join(root_path, "log")
    log_filename = os.path.join(log_dirpath, "timeline.log")
    database_dirpath = os.path.join(root_path, "database")
    database_filename = os.path.join(database_dirpath, "timeline.csv")
    chromedriver_path = os.path.join(root_path, "chromedriver")

    # URL
    stock_url = timeline_url + "?s=in-stock"
    upcoming_url = timeline_url + "?s=upcoming"

    # パラメータ
    timeout = 10  # [s]
    num_scroll_for_migration = 20

    # データベース
    columns = ["name", "url", "is_snkrs_pass", "created_at"]
