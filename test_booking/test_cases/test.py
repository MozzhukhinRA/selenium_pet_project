import pytest
from selenium.webdriver.support.wait import WebDriverWait

from test_booking.test_cases.methods import MethodsMainPageBooking


@pytest.mark.usefixtures('driver')
def test_case_1(driver):
    case = MethodsMainPageBooking(driver, WebDriverWait(driver, 1))
    case.browser_open()
    case.fiend_element_for_click_with_wait()
