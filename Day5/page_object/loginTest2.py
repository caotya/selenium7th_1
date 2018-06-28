from Day5.page_object.loginpage import LoginPage
from Day5.page_object.memberCenterpage import memberCenterPage
from Day5.page_object.myTestCase import MyTestCase


class LoginTest2(MyTestCase):
    def test_login(self):
        login_page = LoginPage(self.driver)
        # 1.打开登录页面
        login_page.open()
        # 2.输入用户名
        login_page.input_username()
        # 3.输入密码
        login_page.input_password()
        # 4.点击登录
        login_page.click_login()
        # 5.验证文本是否登录成功
        member_center_page = memberCenterPage(self.driver)
        self.assertEqual(member_center_page.get_welcome_link_text(), "您好 cty")