# 1.打开浏览器
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(20)
# 2.打开海盗商城网站
driver.get("http://localhost/")
# 3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
# 4.输入用户名和密码
driver.find_element_by_id("username").send_keys("cty")
driver.find_element_by_id("password").send_keys("123456")
# 5.点击登录按钮
driver.find_element_by_class_name("login_btn").click()
# 6.检查登录是否成功
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
if username_text == '您好 cty':
    print("测试通过")
else:
    print("测试失败")
# 7.点击"进入商城购物按钮"
driver.find_element_by_link_text("进入商城购物").click()
# 8. 在商城主页,输入搜索条件"iphone"
driver.find_element_by_class_name("input_ss").send_keys("iphone")
# 9. 点击搜索按钮
driver.find_element_by_class_name("btn1").click()
# 10.在搜索结果页面, 点击第一个商品的图片
driver.find_element_by_class_name("shop_01").click()
#页面跳转
driver.close()
driver.switch_to.window(driver.window_handles[-1])
# 11.点击"加入购物车"
driver.find_element_by_id("joinCarButton").click()