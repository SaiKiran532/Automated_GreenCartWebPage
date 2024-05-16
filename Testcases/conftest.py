import webbrowser
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    # if browser == 'chrome':
    #     driver = webdriver.Chrome()
    #     print("Launching Chrome browser")
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox()
    #     print("Launching Firefox browser")
    # elif browser == 'edge':
    #     driver = webdriver.Firefox()
    #     print("Launching Edge browser")
    # else:
    #     driver = webdriver.Chrome()
    #     print("Launching default Chrome browser")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")




