# 通过ddt代码库,实现数据驱动测试
# 1.导包
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import ddt

# 2.为类增加一个装饰器. 装饰器类似于java中注解
# @ddt.ddt表示这个类实现数据驱动测试
from Day5.csv_register.cvsFileManager import csvfilemanager


@ddt.ddt
class RegisterTest2(unittest.TestCase):
    # 3.声明一个变量,读取csv文件的测试数据
    data_table = csvfilemanager().read('test_data.csv')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

# 4. 为test_register方法添加装饰器@ddt.data, 指定测试数据data_table
    # data_table是一个list类型, 包含很多元素
    # 在data_table前面加一个星号,表示调用ddt.data()方法时
    # 我们传入的不是列表, 而是单独传的列表中的每个元素
    # 所以,星号的作用就是. 把列表中每个元素, 都单独看成一个参数
    # 假如, 一个方法需要的参数数量不固定,我们可以用这种方法
    @ddt.data(*data_table)
    # 5.给方法添加一个参数row
    # 如果想去第一列数据,那么应该是row[1]
    # 使用ddt的方法,相当于把循环写在了方法的外面
    # 好处是, 每次循环, 都相当于重新执行这个方法
    # 这样断言就不会阻塞后面的测试用例了
    def test_register(self, row):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys(row[0])
        driver.find_element(By.NAME, "password").send_keys(row[1])
        driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
        driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
        driver.find_element(By.NAME, "email").send_keys(row[4])

        check_tip = driver.find_element(By.CSS_SELECTOR, "form.registerform.sign > ul > li:nth-child(1) > div > span").text
        self.assertEqual("用户名不低于三位，使用中文、数字、字母皆可！", check_tip)

if __name__ == '__main__':
    unittest.main()