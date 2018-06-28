from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Login:
    def LoginPublicMethods(self,driver):
        driver.get("http://localhost/")
        driver.implicitly_wait(20)
        login_target = driver.find_element_by_link_text("登录")
        driver.execute_script("arguments[0].removeAttribute('target')", login_target)
        login_target.click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("cty")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()