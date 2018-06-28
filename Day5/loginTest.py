import time
import unittest

from Day5.page_object.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        # 自己把这个方法完成
        driver.find_element_by_id("username").send_keys("cty")
        driver.find_element_by_id("password").send_keys("123456")
        old_driver = driver.current_url
        driver.find_element_by_class_name("login_btn").click()
        time.sleep(5)
        new_driver = driver.current_url
        print("登录页面地址："+ old_driver)
        print("登录成功地址："+ new_driver)
        self.assertNotEqual(old_driver,new_driver)

if __name__ == '__main__':
      unittest.main