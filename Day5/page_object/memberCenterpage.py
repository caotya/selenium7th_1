from selenium import webdriver
from selenium.webdriver.common.by import By


class memberCenterPage:
    def __init__(self,driver):
        # driver = webdriver
        self.driver = driver
        self.url="http://localhost/index.php?m=user&c=index&a=index"

    welcome_link_loc = (By.PARTIAL_LINK_TEXT,"您好")
    print(welcome_link_loc)

    def get_welcome_link_text(self):
        return self.driver.find_element(*self.welcome_link_loc).text
