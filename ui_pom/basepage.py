import os
from utilities import config_reader

class BasePage:
    # def __init__(self, driver):
    #     self.driver = driver
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def setup_table_row_attr(self, driver):
        self.driver.execute_script(open("ui_pom/setupAttributes.js").read())

    def get_element(self, locator):
        element = None
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(config_reader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(config_reader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element_by_id(config_reader.readConfig("locators", locator))
        return element

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(config_reader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(config_reader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(config_reader.readConfig("locators", locator)).click()

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(config_reader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(config_reader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(config_reader.readConfig("locators", locator)).send_keys(value)

