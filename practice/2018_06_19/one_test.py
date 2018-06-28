# 1.登录 http://localhost/
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.implicitly_wait(20)
login_target = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_target)
login_target.click()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("cty")
driver.find_element_by_id("password").clear()
ActionChains(driver).send_keys("123456").send_keys(Keys.ENTER).perform()
# 2.返回商城首页
driver.find_element_by_partial_link_text("返回商城首页").click()
# 3.搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
# 4.点击商品（使用javascript删除a标签的target属性）
product_target = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div/div[1]/a")
driver.execute_script("arguments[0].removeAttribute('target')",product_target)
product_target.click()
# 5.在商品详情界面,点击加入购物车
driver.find_element_by_id("joinCarButton").click()
# 6.点击结算按钮
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
# 7.点击添加新地址
driver.find_element_by_css_selector(".add-address").click()
# 8.输入收货人等信息
select_1 = driver.find_element_by_id("add-new-area-select")
select_city = Select(select_1)
select_city.select_by_visible_text("山西省")


select2= driver.find_elements_by_class_name("add-new-area-select")[1]
Select(select2).select_by_visible_text("运城市")

select2= driver.find_elements_by_class_name("add-new-area-select")[2]
Select(select2).select_by_visible_text("新绛县")
# driver.find_element_by_("add-new-area-select").click()
# select_1 = Select()
# select_1.select_by_visible_text("山西省")