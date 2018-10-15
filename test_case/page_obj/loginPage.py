from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class Login(Page):
    """
    用户登录页面元素封装
    """
    url = '/'

    # 跳转登录页面元素
    bbs_avatar_loc = (By.ID, "bbs-avatar")
    bbs_login_loc = (By.ID, "mzLogin")

    # 移动至小人头像并点击"立即登录"
    def bbs_login(self):
        bbs_avatar = self.find_element(*self.bbs_avatar_loc)
        ActionChains(self.driver).move_to_element(bbs_avatar).perform()
        self.find_element(*self.bbs_login_loc).click()

    login_username_loc = (By.ID, "account")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.ID, "login")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一的登录入口
    def user_login(self, username, password):
        """ 获取用户名密码登录 """
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, "//span[@for='account']")
    pawd_error_hint_loc = (By.XPATH, "//span[@for='password']")
    user_login_success_loc = (By.ID, "mzCustName")

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text






