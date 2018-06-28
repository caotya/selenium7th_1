import unittest
from selenium import webdriver

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class FirstUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver= webdriver.Chrome()
        cls.driver.implicitly_wait(20)
    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()
    def test_1(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
    def test_2(self):
        driver = self.driver
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #         除了用name属性切换frame,也可通过8种元素定位方法定位元素,然后切换
        iframe = driver.find_element_by_id("mainFrame")
        driver.switch_to.frame(iframe)
        #         等于driver.switch_to.frame(frame的名字)
        driver.find_element_by_name("name").send_keys("饮水机")
        # 变量名文件名的起名规则:数字,大小写字母,下划线,一般要求以字母开头
        # 如果id是纯数字,用#井号的方式不能定位,
        # 可以用[]的方式定位,所有的属性都可以用[]定位
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id('2').click()
        driver.find_element_by_id("6").click()
        # driver.find_element_by_id("7").cli;ck()
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        select = Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_class_name("button_search").click()
if __name__=='__main__':
    unittest.main()