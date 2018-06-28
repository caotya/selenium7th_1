# 1.登录海盗商城的后台
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.implicitly_wait(20)
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").clear()
ActionChains(driver).send_keys("password").perform()
ActionChains(driver).send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
# 2.选择商品管理模块
driver.find_element_by_link_text("商品管理").click()
# 3.点击添加商品链接
driver.find_element_by_link_text("添加商品").click()
# 4.输入商品名称
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("吹风机")
# 5.选择商品分类(双击或者点击"选当前分类")
driver.find_element_by_css_selector('[id="1"]').click()
driver.find_element_by_css_selector('[id="2"]').click()
driver.find_element_by_css_selector('[id="6"]').click()
double_1 =  driver.find_element_by_css_selector('[id="7"]')
ActionChains(driver).double_click(double_1).perform()
# 6.在下拉框中选择商品品牌
select_1 = driver.find_element_by_name("brand_id")
Select(select_1).select_by_visible_text("苹果 (Apple)")
# 7.点击提交按钮择
driver.find_element_by_css_selector('[value="提交"]').click()