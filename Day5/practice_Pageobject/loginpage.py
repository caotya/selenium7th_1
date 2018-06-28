# http://localhost/index.php?m=user&c=public&a=login
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.url = "http://localhost/index.php?m=user&c=public&a=login"
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")
    def open(self):
        self.driver.get(self.url)

    def username_input(self,username="cty"):
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def password_input(self,password="123456"):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button_loc).click()