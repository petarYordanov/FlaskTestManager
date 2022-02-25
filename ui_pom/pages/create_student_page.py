from ui_pom.basepage import BasePage


class CreateStudentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fillin_submit_create_form(self, firstName, lastName, date):
        self.type("Firstname_field_ID", firstName)
        self.type("Lastname_field_ID", lastName)
        self.type("date_field_ID", date)
        self.click("submit_button_CSS")
