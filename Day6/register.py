from selenium.webdriver.common.by import By

import time

from Day5.page_object.myTestCase import MyTestCase
from Day6.DBconnection import DBconnection


class RegisterTest(MyTestCase):
    def test_register(self):
        # 数据库验证, 测试的正常情况
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys("yangerer")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        driver.find_element(By.NAME, "mobile_phone").send_keys("13922342342")
        driver.find_element(By.NAME, "email").send_keys("adds@sd23a3.com")
        driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(2)
        sql = "select * from hd_user order by id desc;"
        new_record = DBconnection().execute_sql_command(sql)
        self.assertEqual("yangerer",new_record[1])
        self.assertEqual("adds@sd23a3.com", new_record[2])