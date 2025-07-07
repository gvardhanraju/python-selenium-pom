import json
import pytest

from Registration.conftest import browserControl
from Registration.pages.register_page import RegisterPage

register_page_test_data = "C:\\Data\\Python Selenium\\SeleniumCaseStudy\\Registration\\test_data\\registration_data.json"

with open(register_page_test_data) as test_data_file:
    test_data = json.load(test_data_file)
    test_data_list = test_data["data"]

@pytest.mark.parametrize("data", test_data_list)
def test_complete_registration_form(browserControl, data):
    register_page = RegisterPage(browserControl, data)
    register_page.enter_first_name(data["first_name"])
    register_page.enter_last_name(data["last_name"])
    register_page.enter_address(data["address"])
    register_page.enter_email(data["email"])
    register_page.enter_phone(data["phone"])
    register_page.select_male_radio(data["gender"])
    register_page.select_hobbies_checkboxes(data["hobbies"])
    register_page.click_on_language()
    register_page.choose_language(data["languages"])
    register_page.select_skill_option(data["skill"])
    register_page.select_country_option(data["country"])
    register_page.select_year(data["year"])
    register_page.select_month(data["month"])
    register_page.select_day(data["day"])
    register_page.enter_password(data["password"])
    register_page.enter_confirm_password(data["confirm_password"])
    register_page.upload_image(data["image_path"])
    register_page.click_submit_button()
    register_page.take_screenshot(data["screenshot_name"])