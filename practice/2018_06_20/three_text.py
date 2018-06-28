import unittest
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class LoginDeault(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()
    def test_1(self):
        driver = self.driver
        driver.get(" http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys( Keys.ENTER).perform()
    def test_2(self):
        driver = self.driver
        driver.find_element_by_link_text("商品管理").click()
        # 3.点击添加商品链接
        driver.find_element_by_link_text("添加商品").click()
        # 4.输入商品名称
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("name").send_keys("mike")
        # 5.选择商品分类(双击或者点击"选当前分类")
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_css_selector('[id="2"]').click()
        driver.find_element_by_css_selector('[id="6"]').click()
        double = driver.find_element_by_css_selector('[id="7"]').click()
        ActionChains(driver).double_click(double).perform()
        # 6.在下拉框中选择商品品牌
        select1 = driver.find_element_by_name("brand_id")
        Select(select1).select_by_visible_text("苹果 (Apple)")
        # 7.点击提交按钮择
        driver.find_element_by_css_selector('[value="提交"]').click()
if __name__ == '__main__':
    unittest.main()