import unittest
from selenium import webdriver
import time

class Login_Pub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
    def Login(self,user,pwd):
        driver =self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_class_name("login_btn").click()
    def test_1(self):
        self.Login(u"cty",u"123456")
    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()