import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyInfo_Page:
    menu_myinfo_xpath = "//span[text()='My Info']"
    profile_pic_xpath = "//img[@class='employee-image']"
    file_input_xpath = "//input[@type='file']"
    save_button_xpath = "//button[contains(., 'Save')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_myinfo(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.menu_myinfo_xpath))
        ).click()
        time.sleep(2)

    def upload_photo(self, image_path):

        # Step 1 → scroll to image
        pic = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.profile_pic_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", pic)
        time.sleep(1)

        # Step 2 → click image (JS click is required)
        self.driver.execute_script("arguments[0].click();", pic)
        time.sleep(2)

        # Step 3 → upload file (no upload button in OrangeHRM)
        upload_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.file_input_xpath))
        )
        upload_input.send_keys(image_path)
        time.sleep(2)

        # Step 4 → click Save button
        save_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))
        )
        self.driver.execute_script("arguments[0].click();", save_btn)
        time.sleep(2)
