from selenium import webdriver

import time

from Day2.Day2_LoginText import Login

# 1.登录海盗商城e()
driver=webdriver.Chrome()
driver.implicitly_wait(20)
Login().LoginWithDefault(driver)
# 2.点击"账号设置"
driver.find_element_by_link_text("账号设置").click()
# 3.点击"个人资料"
driver.find_element_by_partial_link_text("个人资料").click()
# 4.修改真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("杨一")
# 5.修改性别
#注意注意！！！通过css_selector定位一定要加[]
driver.find_element_by_css_selector('[value="2"]').click()
# driver.find_element_by_id("xb")[2].click()
# driver.find_element_by_xpath('//*[@value="2"]')
# 6.修改生日
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1993-01-01")
# 7.修改QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("727937633")
# 8.点击确定,保存成功
driver.find_element_by_css_selector('[value="确认"]').click()
time.sleep(5)
driver.switch_to.alert.accept()
