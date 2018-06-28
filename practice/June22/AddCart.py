import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

from practice.June22.HomepageLogin import HomepageLogin
class Addcart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls):
        time.sleep()
        cls.driver.quit()
    def test1(self):
        driver =  self.driver
        HomepageLogin().Login(driver)
        # 2.返回商城首页
        driver.find_element_by_partial_link_text("返回商城首页").click()
        # 3.搜索iphone
        driver.find_element_by_name("keyword").send_keys("iphone")
        driver.find_element_by_name("keyword").submit()
        # 4.点击商品（使用javascript删除a标签的target属性）
        product_target = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a")
        driver.execute_script("arguments[0].removeAttribute('target')",product_target)
        product_target.click()
        # 5.在商品详情界面,点击加入购物车
        driver.find_element_by_id("joinCarButton").click()
        # 6.点击结算按钮
        driver.find_element_by_class_name("shopCar_T_span3").click()
        driver.find_element_by_css_selector('.shopCar_btn_03.fl').click()
        # 7.点击添加新地址
        driver.find_element_by_css_selector(".add-address").click()
        # 8.输入收货地区
        select1 =  driver.find_element_by_id("add-new-area-select")
        Select(select1).select_by_visible_text("浙江省")

        select2 = driver.find_elements_by_class_name("add-new-area-select")[1]
        Select(select2).select_by_visible_text("宁波市")

        select3 = driver.find_elements_by_class_name("add-new-area-select")[2]
        Select(select3).select_by_visible_text("江北区")
if __name__ == '__main__':
    unittest.main()