from time import sleep
import sys, unittest
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit
from page_obj.loginPage import Login, MyDynamic
from page_obj.myDynamicPage import MyDynamicPage


class GuanZhu(myunit.MyTest):
    """
    个人中心--我的动态--关注标签页测试
    """

    def test_send_broadcast(self):
        """我的动态--发送广播"""
        Login(self.driver).user_login()
        MyDynamic(self.driver).my_dynamic()
        sleep(1)
        po = MyDynamicPage(self.driver)
        info = "今天心情很好！"
        po.dyamic_input(info)
        po.publish_button()
        sleep(2)
        text = po.new_dynamic()
        self.assertIn(text, info)

    def test_new_rebroadcast(self):
        """我的动态--关注--转播第一条广播"""
        Login(self.driver).user_login()
        MyDynamic(self.driver).my_dynamic()
        sleep(1)
        po = MyDynamicPage(self.driver)
        po.new_rebroadcast()
        po.new_rebroadcast_input("转发此条广播")
        po.new_rebroadcast_button()
        sleep(1)
        text = self.driver.find_element_by_xpath("//*[@class='alert_right']/p").text
        self.assertEqual(text, "转播成功")
        sleep(2)

    def test_new_reply(self):
        """我的动态--关注--回复第一条广播"""
        Login(self.driver).user_login()
        MyDynamic(self.driver).my_dynamic()
        sleep(1)
        po = MyDynamicPage(self.driver)
        po.new_reply()
        info = u"回复此条广播"
        po.new_reply_input(info)
        po.new_reply_button()


if __name__ == '__main__':
    unittest.main()







