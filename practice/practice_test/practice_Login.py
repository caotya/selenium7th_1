# 1.打开浏览器
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# class Login:
#     def LoginWithDeaultInfo(self,driver):
#         print(self)
#         driver = webdriver.Chrome()
#         # 2.打开海盗商城网站
#         driver.get("http://localhost/")
#         driver.implicitly_wait(20)
#         # 3.删除登录链接的target属性
#         # 4.点击登录按钮,跳转到登录页面
#         driver.find_element_by_link_text("登录").click()
#         driver.close()
#         driver.switch_to.window(driver.window_handles[-1])
#         # 5.输入用户名
#         driver.find_element_by_id("username").send_keys("cty")
#         # 6.用键盘输入密码
#         actions = ActionChains(driver)
#         actions.send_keys(Keys.TAB).send_keys("123456").perform()
#         # 7.登陆
#         driver.find_element_by_css_selector('[value="登　录"]').submit()
#         # 8.判断是否登录成功
#         username_text = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/a[1]').text
#         if username_text == '您好 cty':
#             print("succful")
#         else:
#             print("fail")
#         # # # 9.点击进入商城购物
#         # driver.find_element_by_link_text("进入商城购物").click()
#         # # # 10.输入iphone进行搜索
#         # driver.find_element_by_name('keyword').send_keys("iphone")
#         # driver.find_element_by_class_name("btn1").click()
#         # # # 11.点击搜索结果的第一张图片
#         # driver.execute_script('document.getElementsByClassName("shop_01-imgbox")[0].childNodes[1].removeAttribute("target")')
#         # driver.find_element_by_class_name("shop_01").click()
#         # # # 12.加入购物车
#         # driver.find_element_by_id("joinCarButton").click()
#

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Login:
    def LoginDefault(self,driver):
        driver.get("http://localhost/")
        driver.implicitly_wait(20)
        login_target = driver.find_element_by_link_text("登录")
        driver.execute_script("arguments[0].removeAttribute('target')",login_target)
        login_target.click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("cty")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()