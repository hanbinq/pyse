from time import sleep
import sys, unittest, random
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit
from page_obj.loginPage import Login


class LoginTest(myunit.MyTest):
    """社区登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        Login(self.driver).user_login(username, password)

    def test_username_password_null(self):
        """用户名、密码为空登录"""
        self.user_login_verify()
        po = Login(self.driver)
        self.assertEqual(po.user_error_hint(), "账号不能为空")
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")

    def test_password_null(self):
        """用户名正确，密码为空登录"""
        self.user_login_verify(username="18618380370")
        po = Login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")

    def test_username_null(self):
        """用户名为空，密码正确登录"""
        self.user_login_verify(password="123456")
        po = Login(self.driver)
        po.Login(self.driver)
        self.assertEqual(po.user_error_hint(), "账号不能为空")

    def test_login5(self):
        """用户名、密码正确"""
        self.user_login_verify(username="18618380370", password="123456")
        sleep(2)
        po = Login(self.driver)
        self.assertEqual(po.user_login_success(), "qa")


if __name__ == "__main__":
    unittest.main()


