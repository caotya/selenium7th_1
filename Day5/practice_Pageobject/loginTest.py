from Day5.practice_Pageobject.loginpage import LoginPage
from Day5.practice_Pageobject.memberCenterPage import memberCenterPage
from Day5.practice_Pageobject.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.username_input()
        login_page.password_input()
        login_page.click_login()
        member_page = memberCenterPage(self.driver)
        self.assertEqual(member_page.get_welcome_login_text(),"您好 cty")
