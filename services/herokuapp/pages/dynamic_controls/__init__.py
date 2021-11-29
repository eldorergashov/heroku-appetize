import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from services import BasePage
from utility.enumerators import ENV
from utility.helpers import CommonHelper, WebElementHelper
from .dc_vars import *


class DynamicControls(BasePage):

    def __init__(self, env: ENV = None):
        self.config = CommonHelper.json_result_reader(file_name=env.config)
        with allure.step(f"Init Dynamic Controls Page with following env: {env}"):
            if env is None or env is ENV.PROD:
                self.url = self.config["services"]["herokuapp"]["pages"]["dynamic_controls"]["url"]
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
    def click_remove_add_btn(driver: WebDriver) -> None:
        """
        :param driver: Webdriber
        :return: None
        """
        custom_locator = remove_add_btn

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        element.click()

    @staticmethod
    def get_add_remove_btn_text(driver: WebDriver) -> str:
        """
        :param driver: Webdriber
        :return: str: Value of element (latitude)
        """
        custom_locator = remove_add_btn

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        text = element.text.strip('\n×')
        return text

    @staticmethod
    def get_status_text(driver: WebDriver) -> str:
        """
        :param driver: Webdriber
        :return: str: Value of element (latitude)
        """
        custom_locator = checkbox_message

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        text = element.text.strip('\n×')
        return text

    @allure.step("Getting a value from a config file by key: {key}")
    def get_checkbox_status_test_from_config(self, key):
        return self.config["services"]["herokuapp"]["pages"]["dynamic_controls"][key]

    @staticmethod
    def checkbox_displayed(driver: WebDriver) -> bool:
        """
        :param driver: Webdriber
        :return: bool: checkbox is displayed
        """
        custom_locator = a_checkbox

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        return element.is_displayed()

    @staticmethod
    def click_enable_disable_btn(driver: WebDriver) -> None:
        """
        :param driver: Webdriber
        :return: None
        """
        custom_locator = enable_disable_button

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        element.click()

    @staticmethod
    def text_box_enabled(driver: WebDriver) -> bool:
        """
        :param driver: Webdriber
        :return: bool: checkbox is displayed
        """
        custom_locator = text_input_box

        element: WebElement = WebElementHelper.get_element(driver, custom_locator,
                                                           ec_condition=ec.visibility_of_element_located)
        return element.is_enabled()

