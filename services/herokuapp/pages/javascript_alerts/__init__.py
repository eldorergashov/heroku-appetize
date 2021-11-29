import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from services import BasePage
from utility.enumerators import ENV
from utility.helpers import CommonHelper, WebElementHelper
from .js_vars import *


class JavaScriptAlerts(BasePage):

    def __init__(self, env: ENV = None):
        self.config = CommonHelper.json_result_reader(file_name=env.config)
        with allure.step(f"Init Javascript Alerts Page with following env: {env}"):
            if env is None or env is ENV.PROD:
                self.url = self.config["services"]["herokuapp"]["pages"]["javascript_alerts"]["url"]
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

    @allure.step("Getting a value from a config file by key: {key}")
    def get_js_alerts_texts_from_config(self, key):
        return self.config["services"]["herokuapp"]["pages"]["javascript_alerts"][key]

    @staticmethod
    def click_js_alert_btn(driver: WebDriver) -> None:
        """
        :param driver: Webdriber
        :return: None
        """
        custom_locator = js_alert_btn

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        element.click()

    @staticmethod
    def click_js_confirm_btn(driver: WebDriver) -> None:
        """
        :param driver: Webdriber
        :return: None
        """
        custom_locator = js_confirm_btn

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        element.click()

    @staticmethod
    def click_js_prompt_btn(driver: WebDriver) -> None:
        """
        :param driver: Webdriber
        :return: None
        """
        custom_locator = js_prompt_btn

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        element.click()

    @staticmethod
    def get_js_prompt_result_text(driver: WebDriver) -> str:
        """
        :param driver: Webdriber
        :return: str: Value of element (latitude)
        """
        custom_locator = result_message

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        text = element.text.strip('\n×')
        return text

