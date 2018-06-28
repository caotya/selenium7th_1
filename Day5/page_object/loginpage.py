# pageObject类
# 这个类主要做的就是把元素定位和操作改一个易于理解的名字
# driver.get("http://localhost/index.php?m=user&c=public&a=login")
# driver.find_element_by_id("username").send_keys("changcheng")
# driver.find_element_by_id("password").send_keys("123654")
# driver.find_element_by_class_name("login_btn").click()
# 把上面的代码转化成下面的样子
# 1.打开注册页面
# login_page.open()
# 2.输入用户名
# login_page.input_username()
# 3.输入密码
# login_page.input_password()
# 4.点击登录
# login_page.click_login_button()
# 5.验证是否登录成功 --  查看会员中心的用户名显示是否正确
# member_center_page.verify_username()
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    def __init__(self,driver):
        # driver = webdriver.Chrome()
        self.driver = driver
        self.url="http://localhost/index.php?m=user&c=public&a=login"
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID, "password")
    login_button_loc = (By.CLASS_NAME, "login_btn")

    def open(self):
        self.driver.get(self.url)
    def input_username(self,username='cty'):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password='123456'):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button_loc).click()