from ..locators.register_page_locators import RegisterPageLocators
from ..utils.driver_helper import DriverHelper
from Registration.utils.logger import Logger


class RegisterPage:
    def __init__(self, driver, data):
        self.helper = DriverHelper(driver)
        self.driver = driver
        self.data = data
        self.log = Logger.custom_logger(logger_name = self.__class__.__name__)

    def enter_first_name(self, first_name):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.first_name_input, 10)
            self.helper.enter_value(RegisterPageLocators.first_name_input, first_name)
            self.log.info(f"Entered first name as {first_name}")
        except Exception as e:
            self.log.error(f"Failed to enter first name")


    def enter_last_name(self, last_name):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.last_name_input, 10)
            self.helper.enter_value(RegisterPageLocators.last_name_input, last_name)
            self.log.info(f"Entered last name as {last_name}")
        except Exception as e:
            self.log.error(f"Failed to enter last name")

    def enter_address(self, address):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.address_input, 10)
            self.helper.enter_value(RegisterPageLocators.address_input, address)
            self.log.info(f"Entered address as {address}")
        except Exception as e:
            self.log.error(f"Failed to enter address")

    def enter_email(self, email):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.email_input, 10)
            self.helper.enter_value(RegisterPageLocators.email_input, email)
            self.log.info(f"Entered email as {email}")
        except Exception as e:
            self.log.error(f"Failed to enter email")

    def enter_phone(self, phone):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.phone_input, 10)
            self.helper.enter_value(RegisterPageLocators.phone_input, phone)
            self.log.info(f"Entered phone number as {phone}")
        except Exception as e:
            self.log.info(f"Failed to enter phone")

    def select_male_radio(self, gender):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.gender_radio, 10)
            radio_buttons = self.helper.list_of_elements(RegisterPageLocators.gender_radio)
            for radio in radio_buttons:
                if radio.get_attribute("value") == gender:
                    radio.click()
                    break
            self.log.info(f"Selected {gender} radio button")
        except Exception as e:
            self.log.error(f"Failed to select male radio button")

    def select_hobbies_checkboxes(self, hobbies):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.hobbies_checkbox, 10)
            checkboxes = self.helper.list_of_elements(RegisterPageLocators.hobbies_checkbox)
            for checkbox in checkboxes:
                if checkbox.get_attribute("value") in hobbies:
                    checkbox.click()
            self.log.info(f"Checked {hobbies} hobbies")
        except Exception as e:
            self.log.error(f"Failed to check the hobbies")

    def click_on_language(self):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.languages_dropdown, 10)
            self.helper.click_on_element(RegisterPageLocators.languages_dropdown)
            self.log.info(f"Clicked languages dropdown")
        except Exception as e:
            self.log.error(f"Failed to click languages dropdown")

    def choose_language(self, languages_data):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.languages_list, 10)
            languages = self.helper.list_of_elements(RegisterPageLocators.languages_list)
            for language in languages:
                if language.text in languages_data:
                    language.click()
            self.log.info(f"Selected {languages_data} languages")
        except Exception as e:
            self.log.error(f"Failed to select languages")


    def select_skill_option(self, skill):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.skills_dropdown, 10)
            skills = self.helper.selectClass(RegisterPageLocators.skills_dropdown)
            skills.select_by_visible_text(skill)
            self.log.info(f"Selected {skill} skill")
        except Exception as e:
            self.log.error(f"Failed to select skill")

    def select_country_option(self, country):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.countries_dropdown, 10)
            countries = self.helper.selectClass(RegisterPageLocators.countries_dropdown)
            countries.select_by_value(country)
            self.log.info(f"Selected {country} country")
        except Exception as e:
            self.log.error(f"Failed to select country")

    def select_year(self, year_data):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.year_dropdown, 10)
            year = self.helper.selectClass(RegisterPageLocators.year_dropdown)
            year.select_by_value(year_data)
            self.log.info(f"Selected year {year_data}")
        except Exception as e:
            self.log.error(f"Failed to select year")

    def select_month(self, month_data):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.month_dropdown, 10)
            month = self.helper.selectClass(RegisterPageLocators.month_dropdown)
            month.select_by_index(month_data)
            self.log.info(f"Selected month {month_data}")
        except Exception as e:
            self.log.error(f"Failed to select month")

    def select_day(self, day_data):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.day_dropdown, 10)
            day = self.helper.selectClass(RegisterPageLocators.day_dropdown)
            day.select_by_visible_text(day_data)
            self.log.info(f"Selected day {day_data}")
        except Exception as e:
            self.log.error(f"Failed to select day")

    def enter_password(self, password):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.password_input, 10)
            self.helper.enter_value(RegisterPageLocators.password_input, password)
            self.log.info(f"Entered password")
        except Exception as e:
            self.log.error(f"Failed to enter password")

    def enter_confirm_password(self, confirm_password):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.confirm_password_input, 10)
            self.helper.enter_value(RegisterPageLocators.confirm_password_input, confirm_password)
            self.log.info(f"Entered confirm password")
        except Exception as e:
            self.log.error(f"Failed to enter confirm password")

    def upload_image(self, image_path):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.image_upload, 10)
            self.helper.enter_value(RegisterPageLocators.image_upload, image_path)
            self.log.info(f"Uploaded image")
        except Exception as e:
            self.log.error(f"Failed to upload image")

    def click_submit_button(self):
        try:
            self.helper.wait_for_an_element_to_be_visible(RegisterPageLocators.submit_button, 10)
            self.helper.click_on_element(RegisterPageLocators.submit_button)
            self.log.info(f"Clicked submit button")
        except Exception as e:
            self.log.error(f"Failed to click submit button")

    def take_screenshot(self, filename):
        self.helper.captureScreenshot(filename)