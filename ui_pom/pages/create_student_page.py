from ui_pom.basepage import BasePage


class CreateStudentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def submit_create_form(self, firstName, lastName, date):
        self.type("firstname_field_ID", firstName)
        self.type("lastname_field_ID", lastName)
        self.type("date_field_ID", date)
        self.click("submit_button_CSS")
