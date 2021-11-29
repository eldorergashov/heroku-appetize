from pathlib import Path
from typing import Optional, Dict
import time
import random
import allure
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.common.action_chains import ActionChains
from utility.enumerators import STRATEGY


class WebElementHelper:

    @staticmethod
    def get_element(driver: WebDriver, locator: str, strategy: str = "xpath", timeout=None, highlight: bool = True,
                    color: str = "yellow",
                    ec_condition: ec = None) -> WebElement:
        """
        Performs getting WebElement
        :param driver: (WebDriver)
        :param locator: (str) Can be xpath or id
        :param strategy: (str)  Which strategy should be used to find locators. Xpath = Default, ID = support
        :param timeout: (int) Wait before throwing exception
        :param color: (str) Default color to highlight element
        :param highlight: (bool)  Highlight elements by default. Define `False` if you don't want to highlight particular element
        :param ec_condition: (ec) Passing Specific Condition. How to find elements
        :return: (WebElement) WebElement
        """
        if timeout is None:
            self_time = 30
        else:
            self_time = timeout
        try:
            element: WebElement = WebElementHelper.__condition_provider(driver, locator=locator, strategy=strategy,
                                                                        timeout=self_time,
                                                                        ec_condition=ec_condition)
        except StaleElementReferenceException as e:
            for i in range(3):
                wait = WebDriverWait(driver, timeout=self_time, poll_frequency=5)
                element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
                print("LOG - Stale Element Exception: ", e)
                return element
        else:
            if highlight is True:
                WebElementHelper.do_highlight_element(driver, element, color)
            return element

    @staticmethod
    def __condition_provider(driver: WebDriver, locator: str, strategy: str, timeout: int,
                             ec_condition: ec) -> WebElement:
        """
        Find WebElement of the given `strategy` and wait by `ec_condition`
        :param driver: (WebDriver) WebDriver
        :param locator: (str) Can be xpath or id
        :param strategy: (int) Which strategy should be used to find WebElement. Xpath = Default, ID = support
        :param timeout: (int) Wait before throwing exception
        :param ec_condition: (expected_conditions) Passing Specific Condition. How to find elements
        :return: (WebElement)
        """
        wait = WebDriverWait(driver, timeout=timeout)
        if strategy.upper() == STRATEGY.XPATH.name:
            if ec_condition is not None:
                print(f"Locating for: {locator} takes {timeout} seconds")
                element = wait.until(ec_condition((By.XPATH, locator)))
                return element
            element = wait.until(ec.presence_of_element_located((By.XPATH, locator)))
            return element
        elif strategy.upper() == STRATEGY.ID.name:
            ec_custom = ec.presence_of_element_located
            element = wait.until(ec_custom((By.ID, locator)))
            return element

    @staticmethod
    def do_highlight_element(driver: WebDriver, element: WebElement, color: str, effect_time: int = 1.5,
                             border: int = 2) -> None:
        """
        Args:
            driver: (WebDriver) WebDriver passed from Test Case
            element: (WebElement)
            color: (str) Name of Color for highlighting
            effect_time: (int) Time value before border will gone.
            border: (int) Pixel Value for border around element
        Returns: None
        """

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style(f"border: {border}px solid {color};")
        time.sleep(effect_time)
        apply_style(original_style)


class CommonHelper:

    @staticmethod
    def get_project_root() -> Path:
        """
        Performs finding ROOT folder of project
        :return: Path object
        """
        return Path(__file__).parent.parent

    @staticmethod
    def json_result_reader(file_name) -> Dict:
        """
        Open json by provided name  and return
        :param file_name: Name of Config file without extension
        :return: dict
        """
        import json
        path = str(CommonHelper.get_project_root())
        with open(path + '/' + file_name + '.json') as f:
            data = json.load(f)
        return data



