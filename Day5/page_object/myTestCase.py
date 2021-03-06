import unittest
from selenium import webdriver

import time


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()