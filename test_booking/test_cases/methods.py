import time

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_booking.test_cases.conftest import driver


class MethodsMainPageBooking:

    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def browser_open(self):
        self.driver.get('https://www.booking.com/')
        time.sleep(5)

    def fiend_element_for_click_with_wait(self):
        element = self.wait.until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, 'daf5d4cb1c'))
        )
        element.click()
