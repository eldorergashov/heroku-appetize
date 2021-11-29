import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from services import BasePage
from utility.enumerators import ENV
from utility.helpers import CommonHelper, WebElementHelper
from .geolocation_vars import *


class GeoLocation(BasePage):

    def __init__(self, env: ENV = None):
        self.config = CommonHelper.json_result_reader(file_name=env.config)
        with allure.step(f"Init GeoLocation Page with following env: {env}"):
            if env is None or env is ENV.PROD:
                self.url = self.config["services"]["herokuapp"]["pages"]["geo_location"]["url"]
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

    @staticmethod
    def get_latitude_text(driver: WebDriver) -> str:
        """
        :param driver: Webdriber
        :return: str: Value of element (latitude)
        """
        custom_locator = f"//div[@id='lat-value']"

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        text = element.text.strip('\n×')
        return text

    @staticmethod
    def get_longitude_text(driver: WebDriver) -> str:
        """
        :param driver: Webdriber
        :return: str: Value of element (longitude)
        """
        custom_locator = f"//div[@id='long-value']"

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        text = element.text.strip('\n×')
        return text

    @staticmethod
    def click_where_am_i(driver: WebDriver) -> None:
        """
        :param driver: Webdriber
        :return: None
        """
        custom_locator = where_am_i_btn

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        element.click()


