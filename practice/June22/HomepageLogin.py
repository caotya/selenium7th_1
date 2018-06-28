# 前台页面的登录方法
# 需要是否登录成功
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time
class HomepageLogin:
     def Login(self,driver):
        # driver =  webdriver.Chrome()
        driver.get("http://localhost/")
        driver.implicitly_wait(20)
        login_target =  driver.find_element_by_link_text("登录")
        driver.execute_script("arguments[0].removeAttribute('target')",login_target)
        login_target.click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("username").send_keys("cty")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
        usernametext =  driver.find_element_by_link_text("您好 cty").text
        if usernametext == '您好 cty':
            print("测试通过")
        else:
            print("测试失败")