import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_booking.test_cases.conftest import driver
from test_booking.test_cases.selectors.selectors_page import selector
from faker import Faker


class MethodsMainPageBooking:

    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait
        self.selector = selector
        self.fake = Faker()

    def browser_open(self):
        self.driver.get('https://www.booking.com/')
        time.sleep(5)

    def fiend_element_for_click_with_wait(self, selector):
        element = self.wait.until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, selector))
        )
        element.click()

    def type_text_on_field(self, selector):
        element = self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, selector))
        )
        element.send_keys(self.fake.city())
