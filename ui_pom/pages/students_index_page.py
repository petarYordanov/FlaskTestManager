from selenium.webdriver.common.by import By

from ui_pom.basepage import BasePage
from utilities import config_reader


class StudentsIndexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_index_page(self):
        self.driver.get(config_reader.readConfig("environment_data", "base_url"))
        self.setup_table_row_attr(self.driver)

    def searchStudentAndGetDetails(self, firstName, lastName, date):
        self.type("search_field_ID", firstName)
        self.click("table_submit_button_XPATH")
        self.setup_table_row_attr(self.driver)
        studentRow = self.driver.find_element_by_css_selector("tr[firstname='" + firstName + "']")
        if studentRow.get_attribute("lastname") == lastName and studentRow.get_attribute("date") == date:
            studentId = studentRow.get_attribute("id")
            self.driver.find_element_by_xpath("//button[contains(@onclick, 'Students/DETAILS/" + studentId +"')]").click()

    def click_create_new_student(self):
        self.click("create_student_button_XPATH")

    def find_new_student(self, firstName, lastName, date):
        self.setup_table_row_attr(self.driver)
        studentRow = self.driver.find_element_by_css_selector("tr[firstname='" + firstName + "']")
        if studentRow.get_attribute("lastname") == lastName and studentRow.get_attribute("date") == date:
            return studentRow.get_attribute("id")



