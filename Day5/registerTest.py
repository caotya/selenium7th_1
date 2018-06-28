# 这是一个注册页面参数化的方法
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Day5.csv_register.cvsFileManager import csvfilemanager


class RigesterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
    def test_register(self):
        for row in csvfilemanager().read('test_data.csv'):
            driver = self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            driver.find_element(By.NAME, "username").send_keys(row[0])
            driver.find_element(By.NAME, "password").send_keys(row[1])
            driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
            driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME, "email").send_keys(row[4])
            check_text = driver.find_element(By.CSS_SELECTOR,'form.registerform.sign > ul > li:nth-child(1) > div > span').text
            print(check_text)
            self.assertEqual("用户名不低于三位，使用中文、数字、字母皆可！",check_text)
if __name__ == '__main__':
    unittest.main