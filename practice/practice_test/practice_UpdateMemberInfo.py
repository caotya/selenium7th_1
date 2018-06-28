# 1.登录海盗商城
from selenium import webdriver

import time

from Day2.Day2_LoginText import Login

driver = webdriver.Chrome()
driver.implicitly_wait(20)
Login().LoginWithDefault(driver)
# 2.点击"账号设置"
driver.find_element_by_link_text("账号设置").click()
# 3.点击"个人资料"
driver.find_element_by_partial_link_text("个人资料").click()
# 4.修改真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("杨一一")
# 5.修改性别
driver.find_element_by_xpath('//*[@value="1"]').click()
# 6.修改生日
driver.execute_script('document.getElementById("date").removeAttribute("target")')
driver.find_element_by_id("date").send_keys("1991-01-01")
# 7.修改QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("140457890")
# 8.点击确定,保存成功
driver.find_element_by_class_name("btn4").click()
time.sleep(5)
driver.switch_to.alert.accept()