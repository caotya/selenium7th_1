# 1.登录
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/")
# driver.find_element_by_link_text("登录").click()
# driver.close()
# driver.switch_to.window(driver.window_handles[-1])
login_target = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')", login_target)
login_target.click()
driver.find_element_by_id("username").send_keys("cty")
#第一种
# actions = ActionChains(driver)
# actions.send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#第二种
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
# 2.返回商城首页
driver.find_element_by_link_text("进入商城购物").click()
# 3.搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
# 4.点击商品（使用javascript删除a标签的target属性）
product_target = driver.find_element_by_css_selector("body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a")
driver.execute_script("arguments[0].removeAttribute('target')", product_target)
product_target.click()
# 5.在商品详情界面,点击加入购物车
driver.find_element_by_id("joinCarButton").click()
# 6.点击结算按钮
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_css_selector('.shopCar_btn_03.fl').click()
# 7.点击添加新地址
# driver.find_element_by_id("address-box").click()
# 8.输入收货人等信息
driver.find_element_by_css_selector(".add-address").click()
down_select = driver.find_element_by_id("add-new-area-select")
select_province =  Select(down_select)
select_province.select_by_visible_text("山西省")

down_area = driver.find_elements_by_class_name("add-new-area-select")[1]
Select(down_area).select_by_visible_text("运城市")

down_where = driver.find_elements_by_class_name("add-new-area-select")[2]
Select(down_where).select_by_visible_text("绛　县")
# 9.
