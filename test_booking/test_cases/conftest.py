import pytest


@pytest.fixture(scope='function', autouse=True)
def driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()

    prefs = {
        "intl.accept_languages": "en-US,en",
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.page_load_strategy = 'eager'

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()
