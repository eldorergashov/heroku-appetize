from typing import Optional
import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from services import BasePage
from utility.enumerators import ENV
from utility.helpers import WebElementHelper, CommonHelper
from .secure_area_vars import *


class SecurePage(BasePage):

    def __init__(self, env: ENV = None):
        self.config = CommonHelper.json_result_reader(file_name=env.config)
        with allure.step(f"Init Login Page with following env: {env}"):
            if env is None or env is ENV.PROD:
                self.url = self.config["services"]["herokuapp"]["pages"]["secure_page"]["url"]
            elif env is ENV.STAGE:
                raise NotImplementedError
            elif env is ENV.DEV:
                raise NotImplementedError

    def open_page(self, driver: WebDriver) -> None:
        with allure.step(f"Open url: {self.url}"):
            driver.get(self.url)

    def close_page(self, driver: WebDriver) -> None:
        with allure.step(f"Close url: {self.url}"):
            driver.close()

    def verify_page(self, driver: WebDriver) -> None:
        with allure.step(f"Current url: {driver.current_url} asserting {self.url}"):
            assert driver.current_url == self.url

    def get_flash_message_box_text(self, driver: WebDriver, order: Optional = None) -> str:
        """
        :param driver: Webdriber
        :param order: Order of flash messages in box.
        :return: str: Value of element
        """
        if order is not None:
            custom_locator = f"//div[@id='flash'][{order}]"
        else:
            custom_locator = f"//div[@id='flash']"

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        text = element.text.strip('\n×')
        return text

    def get_flash_message_box_test_from_config(self):
        return self.config["services"]["herokuapp"]["pages"]["secure_page"]["secure_logged_in_txt"]
