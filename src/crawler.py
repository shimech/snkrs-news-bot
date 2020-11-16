import os
import time
from dotenv import load_dotenv
from selenium import webdriver
load_dotenv()


class Crawler:
    TIMELINE_URL = os.environ["URL"]
    STOCK_URL = TIMELINE_URL + "?s=in-stock"
    UPCOMING_URL = TIMELINE_URL + "?s=upcoming"
    CHROMEDRIVER_PATH = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "chromedriver")

    @classmethod
    def run(cls, mode="timeline"):
        driver = cls.__init_webdriver()
        time.sleep(3)
        driver.quit()

        target_url = cls.TIMELINE_URL if mode == "timeline" else cls.STOCK_URL
        return [{
            "name": "name",
            "url": target_url,
            "is_snkrs_pass": False
        }]

    @classmethod
    def __init_webdriver(cls):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')

        driver = webdriver.Chrome(
            executable_path=cls.CHROMEDRIVER_PATH,
            desired_capabilities=options.to_capabilities(),
            options=options
        )
        return driver
