import allure
import pytest
from services.herokuapp.pages.login_page import LoginPage
from services.herokuapp.pages.secure_area import SecurePage
from utility.enumerators import ENV


class TestLogin:

    @allure.feature('Login Page')
    @allure.title("Testing login with valid credentials.")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999901", 'Test Case Link')
    @pytest.mark.C999901  #TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_login_valid_creds(self, driver, environment):
        login_page = LoginPage(env=environment)
        login_page.open_page(driver)
        login_page.verify_page(driver)
        login_page.fill_credentials_login(driver, username='tomsmith', password='SuperSecretPassword!')
        secure_page = SecurePage(env=environment)
        secure_page.verify_page(driver)
        text = secure_page.get_flash_message_box_text(driver)
        assert text == secure_page.get_flash_message_box_test_from_config()

    @allure.feature('Login Page')
    @allure.title("Testing login with invalid credentials")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999902", 'Test Case Link')
    @pytest.mark.C999902  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    @pytest.mark.parametrize("username, password, key", [
        ("wrong_username", "SuperSecretPassword!", "invalid_username_txt"),
        ("tomsmith", "wrong_pass", "invalid_password_txt"),
        ("wrong_username", "wrong_pass", "invalid_username_txt")
    ])
    def test_login_invalid_creds(self, driver, environment, username, password, key):
        """Testing 3 different scenarios:
        1 - wrong username, valid password
        2 - valid username, wrong username
        3 - wrong username, wrong password
        """
        login_page = LoginPage(env=environment)
        login_page.open_page(driver)
        login_page.verify_page(driver)
        login_page.fill_credentials_login(driver, username=username, password=password)

        text = login_page.get_flash_message_box_text(driver)
        assert text == login_page.get_flash_message_box_test_from_config(key)




