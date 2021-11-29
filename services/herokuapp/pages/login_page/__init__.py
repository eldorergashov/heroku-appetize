from typing import Optional

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from services import BasePage
from utility.enumerators import ENV
from utility.helpers import CommonHelper, WebElementHelper
from .login_vars import *


class LoginPage(BasePage):

    def __init__(self, env: ENV = None):
        self.config = CommonHelper.json_result_reader(file_name=env.config)
        with allure.step(f"Init Login Page with following env: {env}"):
            if env is None or env is ENV.PROD:
                self.url = self.config["services"]["herokuapp"]["pages"]["login_page"]["url"]
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

    @allure.step("Auth")
    def fill_credentials_login(self, driver: WebDriver, username: str = None, password: str = None) -> None:
        """
         Performs filling credentials into username and password fields by given parameters
        :param driver: Webdriver
        :param username:  Username value
        :param password:  Password Value
        :return: None
        """
        if username is None and password is None:
            username = self.config["services"]["herokuapp"]["pages"]["login_page"]["login_username"]
            password = self.config["services"]["herokuapp"]["pages"]["login_page"]["login_password"]
        wait = WebDriverWait(driver, timeout=30)
        with allure.step(f'Locate Username field by: {username_field} locator'):
            input_field: WebElement = wait.until(ec.element_to_be_clickable(
                (By.XPATH, username_field)))
        with allure.step(f'Insert  "{username}" into Username field '):
            input_field.send_keys(username)
        with allure.step(f'Locate Password Field  by: {password_field} locator'):
            input_password_field: WebElement = wait.until(ec.element_to_be_clickable(
                (By.XPATH, password_field)))
        with allure.step(f'Insert  "******" into Password field '):
            input_password_field.send_keys(password)
        with allure.step(f'Locate Login button  by: {login_button} locator'):
            verify_button: WebElement = wait.until(ec.element_to_be_clickable((By.XPATH, login_button)))
        with allure.step(f'Click on Submit Button with : {login_button} locator'):
            verify_button.click()

    @staticmethod
    def get_flash_message_box_text(driver: WebDriver, order: Optional = None) -> str:
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

    @allure.step("Getting a value from a config file by key: {key}")
    def get_flash_message_box_test_from_config(self, key):
        return self.config["services"]["herokuapp"]["pages"]["login_page"][key]

