"""
Root Module which contains methods to manipulate followings:
1. Test Sessions
2. Test Cases
4. WebDrivers
"""
import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utility.enumerators import BROWSERS
from utility.helpers import CommonHelper

driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    """
    Add screenshot for failed test cases
    :param item: A basic test invocation item.
    :param call:
    :return: None
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # Add screenshot of allure report
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('Add failed screenshot'):
                allure.attach(driver.get_screenshot_as_png(), "Failed screenshot", allure.attachment_type.PNG)


@pytest.fixture
def browser_name(request) -> str:
    """
    Fixture which getting cmd argument `--browser` and return name of browser based on argument value.
    Args:
        request:
    Returns: (str) browser name from `BROWSERS` enumerator
    """
    br_name = request.config.getoption("--browser").upper()
    if br_name == BROWSERS.CHROME.name:
        return BROWSERS.CHROME.name
    elif br_name == BROWSERS.FIREFOX.name:
        return BROWSERS.FIREFOX.name


@pytest.fixture(scope='function')
def driver(browser_name: str, max_windows: bool = True):
    """
    This fixture will be used by test cases to get a WebDriver instance
    :param browser_name: Name of browser for test. Example: chrome, opere, firefox
    :param max_windows: Flag for browser screen maximizing
    :param browser_log: Flag to gather browser log
    :return: WebDriver
    """
    global driver
    if browser_name == BROWSERS.CHROME.name:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        if max_windows:
            driver.maximize_window()
        yield driver
        driver.quit()

def pytest_addoption(parser):
    """
    Pytest Hook to capture cmd argument
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to test")
    parser.addoption("--env", action="store", dest="environment", choices=(
        "PROD", "STAGE", "DEV",),
        default="",
        help="",
    )

# def pytest_collection_modifyitems(config, items):
#     # get value from argument of --env
#     env = config.getoption("--env")
#     # init a skip mark with description
#     skip_custom_mark = pytest.mark.skip(reason="Env for this test out of scope for this execution")
#     # iterate for all tests
#     for count, item in enumerate(items):
#         # iterate for parametrize makr object
#         for x in item.iter_markers(name="parametrize"):
#             # for env we need only  `environment` to avoid parsing another parametrize like `section` etc
#             if x.args[0] == "environment":
#                 # env_list is a list with Enums
#                 env_list = x.args[1]
#                 #  env_list[count].title to get a string from enum  and compare with cmd argument str
#                 if env_list[count].title != env:
#                     # assign marker for test
#                     item.add_marker(skip_custom_mark)


