import datetime
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Registration.utils.logger import Logger


class DriverHelper:

    def __init__(self, driver):
        self.driver = driver
        self.log = Logger.custom_logger(logger_name=self.__class__.__name__)

    def wait_for_an_element_to_be_visible(self, locator, time):
        try:
            wait = WebDriverWait(self.driver, time)
            wait.until(ec.visibility_of_element_located(locator))
        except Exception as e:
            self.log.error(e)

    def click_on_element(self, locator):
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            self.log.error(e)

    def enter_value(self, locator, value):
        try:
            self.driver.find_element(*locator).send_keys(value)
        except Exception as e:
            self.log.error(e)

    def get_text(self, locator):
        try:
            return self.driver.find_element(*locator).text
        except Exception as e:
            self.log.error(e)
            return None

    def get_title(self):
        try:
            return self.driver.title
        except Exception as e:
            self.log.error(e)
            return None

    def list_of_elements(self, locator):
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            self.log.error(e)
            return None

    def selectClass(self, locator):
        try:
            return Select(self.driver.find_element(*locator))
        except Exception as e:
            self.log.error(e)
            return None

    def captureScreenshot(self, filename):
        time_stamp = datetime.datetime.now()
        time_stamp = time_stamp.strftime("%d-%m-%Y_%I.%M.%S_%p")
        file_path = "C:\\Data\\Python Selenium\\SeleniumCaseStudy\\Registration\\reports\\screenshots\\" + filename + "_" + str(time_stamp) + ".png"
        self.driver.get_screenshot_as_file(file_path)
        time.sleep(2) # To capture the screenshot
