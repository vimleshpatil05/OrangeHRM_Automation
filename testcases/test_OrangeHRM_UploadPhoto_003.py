import pytest
import allure
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.MyInfo_Page import MyInfo_Page
from Utilities.readConfig import ReadConfig
from Utilities.logger import Logger_class

@pytest.mark.usefixtures("driver_setup")
class Test_Upload_Profile_Photo_003:

    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    log = Logger_class.get_logger()

    @allure.title("Upload Profile Photo in My Info")
    @allure.description("This test logs in and uploads a profile photo in My Info")
    @pytest.mark.regression
    def test_upload_profile_photo(self):

        self.log.info("Navigating to Login Page")
        self.driver.get(self.login_url)

        lp = Login_Page_Class(self.driver)
        lp.Enter_Username(self.username)
        lp.Enter_Password(self.password)
        lp.Click_Login()

        assert lp.verify_login() == "Login Successful", "Login Failed"

        myinfo = MyInfo_Page(self.driver)
        myinfo.open_myinfo()

        image_path = r"E:\Credence\OrangeHRM\download.jpg"
        myinfo.upload_photo(image_path)

        self.log.info("Profile photo uploaded successfully!")
        assert True
