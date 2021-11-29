import time

import allure
import pytest
from selenium import webdriver
from services.herokuapp.pages.javascript_alerts import JavaScriptAlerts
from utility.enumerators import ENV


class TestJavaScriptAlerts:

    @allure.feature('JavaScript Alerts Page')
    @allure.title("Testing JavaScript Alerts - JS Alert")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999906", 'Test Case Link')
    @pytest.mark.C999906  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_js_alert(self, driver, environment):
        js_alerts_page = JavaScriptAlerts(env=environment)
        js_alerts_page.open_page(driver)
        js_alerts_page.verify_page(driver)
        js_alerts_page.click_js_alert_btn(driver)
        alert = driver.switch_to.alert
        text = alert.text
        assert text == js_alerts_page.get_js_alerts_texts_from_config("js_alert_text")
        alert.accept()

    @allure.feature('JavaScript Alerts Page')
    @allure.title("Testing JavaScript Alerts - JS Confirm")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999907", 'Test Case Link')
    @pytest.mark.C999907  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_js_confirm(self, driver, environment):
        js_alerts_page = JavaScriptAlerts(env=environment)
        js_alerts_page.open_page(driver)
        js_alerts_page.verify_page(driver)
        js_alerts_page.click_js_confirm_btn(driver)
        alert = driver.switch_to.alert
        text = alert.text
        assert text == js_alerts_page.get_js_alerts_texts_from_config("js_confirm_text")
        alert.accept()

    @allure.feature('JavaScript Alerts Page')
    @allure.title("Testing JavaScript Alerts - JS Prompt")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999908", 'Test Case Link')
    @pytest.mark.C999908  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_js_prompt(self, driver, environment):
        js_alerts_page = JavaScriptAlerts(env=environment)
        js_alerts_page.open_page(driver)
        js_alerts_page.verify_page(driver)
        js_alerts_page.click_js_prompt_btn(driver)
        alert = driver.switch_to.alert
        text = alert.text
        assert text == js_alerts_page.get_js_alerts_texts_from_config("js_prompt_text")
        alert.send_keys(js_alerts_page.get_js_alerts_texts_from_config("js_prompt_input_text"))
        alert.accept()
        # verifying that the text we entered is showing up in a result message
        assert 'You entered: ' + js_alerts_page.get_js_alerts_texts_from_config("js_prompt_input_text") == js_alerts_page.get_js_prompt_result_text(driver)
        # this sleep is for demo purposes
        time.sleep(3)

