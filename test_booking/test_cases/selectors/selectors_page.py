from dataclasses import dataclass


@dataclass
class SelectorBookingMainPage:
    select_popup_cookies = 'ot-button-order-1'
    select_popup_reg = 'daf5d4cb1c'
    select_field_city = 'b915b8dc0b'
    select_city_on_list = 'e03644d405:nth-child(1)'
    select_datetime_moth = 'af236b7586:nth-child(1)'
    select_datetime_day = 'ecb788f3b7'


selector = SelectorBookingMainPage
for_dev = SelectorBookingMainPage
