import allure
import pytest
from services.herokuapp.pages.dynamic_controls import DynamicControls
from utility.enumerators import ENV


class TestDynamicControls:

    @allure.feature('Dynamic Controls Page')
    @allure.title("Testing Dynamic Controls add/remove button.")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999904", 'Test Case Link')
    @pytest.mark.C999904  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_dynamic_controls_add_remove(self, driver, environment):
        dynamic_controls_page = DynamicControls(env=environment)
        dynamic_controls_page.open_page(driver)
        dynamic_controls_page.verify_page(driver)
        dynamic_controls_page.click_remove_add_btn(driver)
        text_removed = dynamic_controls_page.get_status_text(driver)
        # verifying that the checkbox has been removed by verifying the status text
        assert text_removed == dynamic_controls_page.get_checkbox_status_test_from_config("gone_text")
        # verifying that the checkbox is not present
        assert not len(driver.find_elements_by_xpath("//input[@type='checkbox']"))
        dynamic_controls_page.click_remove_add_btn(driver)
        text_added = dynamic_controls_page.get_status_text(driver)
        # verifying that the checkbox has been added by verifying the status text
        assert text_added == dynamic_controls_page.get_checkbox_status_test_from_config("added_text")
        # verifying that the checkbox is present/displayed
        assert dynamic_controls_page.checkbox_displayed(driver)

    @allure.feature('Dynamic Controls Page')
    @allure.title("Testing Dynamic Controls Enable/Disable functionality.")
    @allure.testcase("https://spoton.testrail.io/index.php?/cases/view/999905", 'Test Case Link')
    @pytest.mark.C999905  # TestRail ID
    @pytest.mark.smoke
    @pytest.mark.parametrize("environment", [ENV.PROD])
    def test_dynamic_controls_enable_disable(self, driver, environment):
        dynamic_controls_page = DynamicControls(env=environment)
        dynamic_controls_page.open_page(driver)
        dynamic_controls_page.verify_page(driver)
        dynamic_controls_page.click_enable_disable_btn(driver)
        text_enabled = dynamic_controls_page.get_status_text(driver)
        # verifying that the input box has been enabled by verifying the status text
        assert text_enabled == dynamic_controls_page.get_checkbox_status_test_from_config("enabled_text")
        # verifying that the input box/element is enabled
        assert dynamic_controls_page.text_box_enabled(driver)
        dynamic_controls_page.click_enable_disable_btn(driver)
        text_disabled = dynamic_controls_page.get_status_text(driver)
        # verifying that the input box has been disabled by verifying the status text
        assert text_disabled == dynamic_controls_page.get_checkbox_status_test_from_config("disabled_text")
        # verifying that the input box/element is disabled
        assert dynamic_controls_page.text_box_enabled(driver) is False

