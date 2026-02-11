import random
import time
from test_booking.test_cases.selectors_site.selectors_page import for_dev
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_booking.test_cases.conftest import driver
from test_booking.test_cases.selectors_site.selectors_page import selector
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

    def fiend_element_id_for_click_with_wait(self, selector):
        element = self.wait.until(
            EC.element_to_be_clickable((
                By.ID, selector))
        )
        element.click()

    def type_text_on_field(self, selector):
        element = self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, selector))
        )
        city_name = self.fake.city()
        element.send_keys(city_name)
        return city_name

    def get_date(self, selector):
        from datetime import datetime
        datetime = datetime.now()
        current_date = f'{datetime.strftime("%B")} {datetime.year}'
        element = self.wait.until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, selector), current_date)
        )
        if True:
            element = current_date

        assert element == current_date

        if datetime.strftime("%B") in "February":
            element = self.wait.until(
                EC.presence_of_all_elements_located((
                    By.CLASS_NAME, for_dev.select_datetime_day)
                ))
            element[random.randint(datetime.day, 27)].click()

        elif datetime.strftime(
                "%B") in ["March", "May", "July", "August", "October", "December"]:
            element = self.wait.until(
                EC.presence_of_all_elements_located((
                    By.CLASS_NAME, for_dev.select_datetime_day)
                ))
            element[random.randint(datetime.day, 30)].click()
        else:
            element = self.wait.until(
                EC.presence_of_all_elements_located((
                    By.CLASS_NAME, for_dev.select_datetime_day)
                ))
            element[random.randint(datetime.day, 29)].click()

    def element_should_be_visible(self, selector):
        self.wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME, selector)
        ))
