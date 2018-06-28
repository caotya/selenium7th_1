#这是一个登陆的封装类
# 1.打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Login:
    def LoginWithDefault(self,driver):
        #driver = webdriver.Chrome()
        # 2.打开海盗商城网站
        driver.get("http://localhost/")
        # 3.删除登录链接的target属性
        driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
        # 4.点击登录按钮,跳转到登录页面
        driver.find_element_by_link_text("登录").click()
        # 5.输入用户名
        driver.find_element_by_id("username").send_keys("cty")
        # 6.输入密码
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).send_keys("123456").perform()
        # 7.登陆
        driver.find_element_by_class_name("login_btn").submit()