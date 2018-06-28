import unittest
from selenium import webdriver

import time

from practice.June22.HomepageLogin import HomepageLogin
class ModifySelfData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
    def test_1(self):
        driver = self.driver
        HomepageLogin().Login(driver)
        driver.implicitly_wait(20)
        driver.find_element_by_link_text("账号设置").click()
        driver.find_element_by_partial_link_text("个人资料").click()
        driver.find_element_by_css_selector('[value="0"]').click()
        datetest = driver.find_element_by_id("date")
        driver.execute_script("arguments[0].removeAttribute('readonly')",datetest)
        driver.find_element_by_id("date").send_keys("1776-01-09")
        driver.find_element_by_css_selector('[value="确认"]').click()
        time.sleep(10)
        driver.switch_to.alert.accept()
if __name__ == '__main__':
    unittest.main()