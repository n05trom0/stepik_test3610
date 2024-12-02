import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: e.g. en, fr, es, etc.")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print(f"\nStarting browser with language: {language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuitting browser...")
    browser.quit()