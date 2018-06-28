import unittest
from selenium import webdriver

import time

from practice.UpadteInformation.LoginPublicMethods import Login
driver =  webdriver.Chrome()
driver.implicitly_wait(20)
Login().LoginPublicMethods(driver)

# 2.点击"账号设置"

driver.find_element_by_link_text("账号设置").click()
# 3.点击"个人资料"
driver.find_element_by_link_text("个人资料").click()
# 4.修改真实姓名
# 5.修改性别
driver.find_element_by_css_selector('[value="2"]').click()
# 6.修改生日
shengri = driver.find_element_by_id("date")
driver.execute_script("arguments[0].removeAttribute('readonly')",shengri)
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1991-02-07")
# 7.修改QQ

# 8.点击确定,保存成功
driver.find_element_by_css_selector('[value="确认"]').click()
time.sleep(5)
driver.switch_to.alert.accept()


