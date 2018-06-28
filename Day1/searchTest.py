# 1.打开主页
from selenium import webdriver
drives=webdriver.Chrome()
drives.implicitly_wait(20)
drives.get("http://localhost/")
# 2.点击登录按钮
drives.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/a[1]").click()
# 3.在搜索框中输入iphone
drives.switch_to.window(drives.window_handles[-1])
drives.find_element_by_name("keyword").send_keys("iphone")