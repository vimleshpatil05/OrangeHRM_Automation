import pytest
import allure

from Utilities.XLUtils import XLUtils_class
from Utilities.logger import Logger_class
from pageObjects.Login_Page import Login_Page_Class
from Utilities.readConfig import ReadConfig
@pytest.mark.usefixtures("driver_setup")
class  Test_OrangeHRM_Login_DDT_002:
    driver = None
    login_url = ReadConfig.get_login_url()
    log = Logger_class.get_logger()
    excel_file = ".\\Test_Data\\OrangeHRM_Test_Data.xlsx"
    sheet = "Sheet1"

    def test_OrangeHRM_Login_DDT_003(self):
        self.log.info("Starting Test: Verify OrangeHRM Login Functionality")
        row_count = XLUtils_class.get_row_count(self.excel_file, self.sheet)
        self.log.info(f"Total Rows in Excel: {row_count}")
        result = []
        for i in range(2, row_count + 1):
            username = XLUtils_class.read_data(self.excel_file, self.sheet, i, 2)
            password = XLUtils_class.read_data(self.excel_file, self.sheet, i, 3)
            expected_result = XLUtils_class.read_data(self.excel_file, self.sheet, i, 4)
            self.log.info(f"Test Data: Username={username}, Password={password}, Expected Result={expected_result}")
            self.log.info("Navigating to OrangeHRM Login Page")
            self.driver.get(self.login_url)
            self.log.info("OrangeHRM Login Page Loaded")
            lp = Login_Page_Class(self.driver)
            lp.Enter_Username(username)
            lp.Enter_Password(password)
            lp.Click_Login()
            if lp.verify_login() == "Login Successful":
                self.log.info(f"Login Successful for Username={username}")
                self.driver.save_screenshot(f"screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png")
                allure.attach.file(f"screenshots\\test_OrangeHRM_Login_DDT_003_pass_{username}.png", name=f"test_OrangeHRM_Login_DDT_003_pass_{username}", attachment_type=allure.attachment_type.PNG)
                lp.Click_Menu()
                lp.Click_Logout()

                actual_result = "Login Successful"
            else:
                self.log.error(f"Login Failed for Username={username}")
                self.driver.save_screenshot(f"screenshots\\test_OrangeHRM_Login_DDT_003_fail_{username}.png")
                allure.attach.file(f"screenshots\\test_OrangeHRM_Login_DDT_003_fail_{username}.png", name=f"test_OrangeHRM_Login_DDT_003_fail_{username}", attachment_type=allure.attachment_type.PNG)

                actual_result = "Login Failed"

            if actual_result == expected_result:
                self.log.info(f"Test Passed for Username={username}")
                test_status = "Pass"
                result.append("Pass")
            else:
                self.log.error(f"Test Failed for Username={username}")
                test_status = "Fail"
                result.append("Fail")
            XLUtils_class.write_data(self.excel_file, self.sheet, i, 5, test_status)
        self.log.info(f"Test Results: {result}")

        assert "Fail" not in result
        self.log.info("test_OrangeHRM_Login_DDT_003 test Completed")
        self.log.info("=============================================================")

# pytest -v -n=auto --html=Html_Reports\OrangeHRM_Login.html --alluredir=Allure_Reports --browser chrome
# 15 Dec 2025 --> 7th Feb 2026 --> 54 days
# Python-Selenium-Pytest-Git-Jenkins

# Task 1 :
# image upload

# Task 2 :
# bank app minimum 10 testcases

# Task 3 :
# http://uitestingplayground.com/ --> Money rewards

# Task 4 :
# dynamic Xpath
# partial Xpath/ 'or' and 'and'

# task 5
# explore other automation tools/frameworks



