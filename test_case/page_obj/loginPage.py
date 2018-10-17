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


class MyDynamic(Page):
    """
    用户中心--我的动态
    """
    my_username_loc = (By.ID, "mzCustName")
    my_account_loc = (By.CLASS_NAME, "actmanage_mzcust")
    my_dynamic_loc = (By.LINK_TEXT, "我的动态")
    my_invitation_loc = (By.LINK_TEXT, "我的帖子")

    # 我的账号
    def my_account(self):
        above = self.find_element(*self.my_username_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.my_account_loc).click()

    url = "/home.php?mod=follow"   # 我的动态链接

    def open(self):
        self._open(self.url)

    # 我的动态
    def my_dynamic(self):
        self.open()


class MyInvitation(Page):
    """
    用户中心--我的帖子
    """
    url = "/forum.php?mod=guide&view=my"   # 我的帖子

    def open(self):
        self._open(self.url)

    # 我的帖子
    def my_invitation(self):
        self.open()


class MyFriend(Page):
    """
    用户中心--我的好友
    """
    url = "/home.php?mod=space&do=friend"  # 我的好友

    def open(self):
        self._open(self.url)

    # 我的好友
    def my_friend(self):
        self.open()


class MySetting(Page):
    """
    用户中心--我的设置
    """

    url = "/home.php?mod=spacecp&ac=profile&op=base"   # 我的设置

    def open(self):
        self._open(self.url)

    # 我的好友
    def my_setting(self):
        self.open()


class MyVest(Page):
    """
    用户中心--我的马甲
    """

    url = "/home.php?mod=spacecp&ac=plugin&id=myrepeats:memcp"   # 我的马甲

    def open(self):
        self._open(self.url)

    # 我的马甲
    def my_vest(self):
        self.open()

if __name__ == '__main__':
    pass






