from ui_pom.basepage import BasePage


class StudentDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def userDetailsFromDescriptionList(self):
        userDetailsElements = self.driver.find_elements_by_css_selector(".dl-horizontal>dd")
        return {"firstName": userDetailsElements[0],
                "lastName": userDetailsElements[1],
                "date": userDetailsElements[2]}

        
