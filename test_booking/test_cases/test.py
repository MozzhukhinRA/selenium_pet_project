import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from test_booking.test_cases.page_object_methods import MethodsMainPageBooking
from test_booking.test_cases.selectors.selectors_page import selector


@pytest.mark.usefixtures('driver')
@allure.severity(allure.severity_level.BLOCKER)
def test_case_1(driver):
    case = MethodsMainPageBooking(driver, WebDriverWait(driver, 1))
    with allure.step('Open Booking home page'):
        case.browser_open()
    with allure.step('To close modal window'):
        case.fiend_element_for_click_with_wait(selector.select_popup_reg)
    with allure.step('Tap on field city'):
        case.fiend_element_for_click_with_wait(selector.select_field_city)
    with allure.step('Type text - City Name'):
        case.type_text_on_field(selector.select_field_city)
    with allure.step('In the visible list, choose first city'):
        case.fiend_element_for_click_with_wait(selector.select_city_on_list)
