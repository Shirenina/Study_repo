from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language to start a browser: ")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nStart chrome browser for test...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser...")
    browser.quit()
