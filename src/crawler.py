import os
import gc
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from config import Config
from utils import Utils


class Crawler:
    def __init__(self, is_migrate, logger):
        self.is_migrate = is_migrate
        self.logger = logger
        self.driver = self.__init_webdriver()
        self.wait = WebDriverWait(self.driver, Config.timeout)

    def execute(self):
        if self.is_migrate:
            self.__migrate()
            return None, None
        else:
            return self.__run()

    def __run(self):
        Utils.make_dir(Config.database_dirpath)
        df = self.__get_dataframe(Config.database_filename)

        try:
            self.driver.get(Config.upcoming_url)
            time.sleep(1)

            error_message = self.__move_to_timeline_page()
            if error_message is not None:
                self.logger.error(error_message)
                self.__release_driver()
                return [], df

            card_dicts, error_message = self.__get_card_dicts()
            self.__release_driver()
            if error_message is not None:
                self.logger.error(error_message)
                return [], df
            if len(card_dicts) == 0:
                return card_dicts, df

            news_list = []
            for card_dict in card_dicts:
                if not card_dict.get("url") in df["url"].values.tolist():
                    news = card_dict
                    news["is_snkrs_pass"] = ("pass" in card_dict["url"])
                    news_list.append(news)
                    df = df.append(news, ignore_index=True)
                    self.logger.info("New Post: {}".format(news))
            self.logger.info(
                "{} new posts were detected.".format(len(news_list)))

            return news_list, df

        except TimeoutException as e:
            self.logger.error("TIMEOUT")
            self.__release_driver()
            return [], df

    def __migrate(self):
        Utils.make_dir(Config.database_dirpath)
        df = self.__get_dataframe(Config.database_filename)

        try:
            self.driver.get(Config.upcoming_url)
            time.sleep(1)

            error_message = self.__move_to_timeline_page()
            if error_message is not None:
                self.logger.error(error_message)
                self.__release_driver()
                return

            self.__move_to_bottom_of_page()

            error_message = self.__push_show_more_button()
            if error_message is not None:
                self.logger.error(error_message)
                self.__release_driver()
                return

            for _ in range(Config.num_scroll_for_migration):
                self.__move_to_bottom_of_page()
                time.sleep(1)
                self.wait.until(EC.presence_of_all_elements_located)

            card_dicts, error_message = self.__get_card_dicts()
            self.__release_driver()
            if error_message is not None:
                self.logger.error(error_message)
                return
            if len(card_dicts) == 0:
                return

            for card_dict in card_dicts:
                news = card_dict
                news["is_snkrs_pass"] = ("pass" in card_dict["url"])
                df = df.append(news, ignore_index=True)
            df.to_csv(Config.database_filename, index=False)
            self.logger.info("Complete migration.")

        except TimeoutException as e:
            self.logger.error("TIMEOUT")
            self.__release_driver()

    def __init_webdriver(self, driver_path=Config.chromedriver_path):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome(
            executable_path=driver_path,
            desired_capabilities=options.to_capabilities(),
            options=options
        )
        return driver

    def __get_dataframe(self, filename, columns=Config.columns):
        if os.path.exists(filename) and self.is_migrate is False:
            return pd.read_csv(filename)
        else:
            df = pd.DataFrame(columns=columns)
            df.to_csv(filename, index=False)
            self.logger.info("CSV: {} was made.".format(filename))
            return df

    def __move_to_timeline_page(self):
        nav_items = self.driver.find_elements_by_class_name("nav-items")
        if nav_items is None:
            return "nav_items were not found."

        for nav_item in nav_items:
            if nav_item.text == "タイムライン":
                nav_item.click()
                self.logger.info("Move to timeline page.")
                time.sleep(3)
                return

    def __move_to_bottom_of_page(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("Move to bottom of page.")

    def __push_show_more_button(self):
        buttons = self.driver.find_elements_by_tag_name("button")
        if buttons is None:
            return "buttons were not found."

        for button in buttons:
            if button.text == "もっと見る":
                button.click()
                self.logger.info("Push show more button.")
                self.wait.until(EC.presence_of_all_elements_located)
                return

    def __get_card_dicts(self):
        card_links = self.driver.find_elements_by_class_name("card-link")
        if card_links is None:
            return [], "card_links were not found."

        card_dicts = []
        for card_link in card_links:
            name = card_link.get_attribute("aria-label")
            url = card_link.get_attribute("href")
            if name is not None and url is not None:
                card_dicts.append({
                    "name": name,
                    "url": url,
                    "created_at": Utils.get_time_now()
                })
            else:
                self.logger.error(
                    "Missing information (name={}, url={})".format(name, url))
        self.logger.info("{} cards were detected.".format(len(card_dicts)))
        return card_dicts, None

    def __release_driver(self):
        self.driver.quit()
        del self.driver
        gc.collect()
