import traceback

from selenium import webdriver

from ui_pom.pages.create_student_page import CreateStudentPage
from ui_pom.pages.student_details_page import StudentDetailsPage
from ui_pom.pages.students_index_page import StudentsIndexPage


class TestData:
    def __init__(self):
        self.firstName = 'crucious'
        self.lastName = 'labbo'
        self.date = '1/21/2022 12:00:00 AM'

class TestDataCreate:
    def __init__(self):
        self.firstName = ''
        self.lastName = '1'
        self.date = '1/21/2022 12:00:00 AM'

class EndToEndTests:
    def __init__(self):
        self.testData = TestData()
        self.testDataCreate = TestDataCreate()
        self.driver = webdriver.Firefox(executable_path="ui_pom/geckodriver.exe")
        self.index_page = StudentsIndexPage(self.driver)
        self.details_page = StudentDetailsPage(self.driver)
        self.new_student_page = CreateStudentPage(self.driver)

    def test_get_student_details(self):
        try:
            self.index_page.open_index_page()
            self.index_page.searchStudentAndGetDetails(self.testData.firstName,
                                                                         self.testData.lastName, self.testData.date)
            userDetailsFound = self.details_page.userDetailsFromDescriptionList()
            if (userDetailsFound["firstName"].text == self.testData.firstName
                    and userDetailsFound["lastName"].text == self.testData.lastName
            and userDetailsFound["date"].text == self.testData.date):
                return {'Test Category': 'E2E Tests',
                        'Test_name': 'Get Student Details',
                        'Step 1': "Open student index page",
                        'Step 2': "Search for student in a table row by id",
                        'Step 3': "Click on Details button from the table row",
                        'Step 4': "Verify first name, last name and date at Details Page",
                        'Test outcome': 'PASSED'
                        }
            else:
                return {'Test Category': 'E2E Tests',
                        'Test_name': 'Get Student Details',
                        'Step 1': "Open student index page",
                        'Step 2': "Search for student in a table row by id",
                        'Step 3': "Click on Details button from the table row",
                        'Step 4': "Verify first name, last name and date at Details Page",
                        'Test outcome': 'FAILED'
                        }
        except Exception:
            return {'Test Category': 'E2E Tests',
             'Test_name': 'Get Student Details',
             'Step 1': "Open student index page",
             'Step 2': "Search for student in a table row by id",
             'Step 3': "Click on Details button from the table row",
             'Step 4': "Verify first name, last name and date at Details Page",
             'Test outcome': 'FAILED',
                    'Exception': str(traceback.print_exc())
             }

    def test_create_new_student(self):
        try:
            self.index_page.open_index_page()
            self.index_page.click_create_new_student()
            self.new_student_page.submit_create_form(self.testDataCreate.firstName, self.testDataCreate.lastName, self.testDataCreate.date )
            studentId = self.index_page.find_new_student(self.testDataCreate.firstName, self.testDataCreate.lastName, self.testDataCreate.date)
            if(int(studentId).real):
                return {'Test Category': 'E2E Tests',
                        'Test_name': 'Create New Student',
                        'Step 1': "Open student index page",
                        'Step 2': "Click on create new student",
                        'Step 3': "At create new student page, fill in and submit Form",
                        'Step 4': "Find new student created in the index page table",
                        'Test outcome': 'PASSED'
                        }
            else:
                return {'Test Category': 'E2E Tests',
                        'Test_name': 'Create New Student',
                        'Step 1': "Open student index page",
                        'Step 2': "Click on create new student",
                        'Step 3': "At create new student page, fill in and submit Form",
                        'Step 4': "Find new student created in the index page table",
                        'Test outcome': 'FAILED'
                        }
        except Exception:
            return {'Test Category': 'E2E Tests',
                    'Test_name': 'Create New Student',
                    'Step 1': "Open student index page",
                    'Step 2': "Click on create new student",
                    'Step 3': "At create new student page, fill in and submit Form",
                    'Step 4': "Find new student created in the index page table",
                    'Test outcome': 'FAILED',
                    'Exception': str(traceback.print_exc())
                    }


