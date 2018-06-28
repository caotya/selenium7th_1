from selenium.webdriver.common.by import By


class memberCenterPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"
    welcome_login_text = (By.PARTIAL_LINK_TEXT,"您好")
    def get_welcome_login_text(self):
        return self.driver.find_element(*self.welcome_login_text).text