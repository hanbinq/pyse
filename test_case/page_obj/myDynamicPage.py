from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep


class MyDynamicPage(Page):
    """
    个人中心--我的动态
    """
    # Action
    broadcast_number_loc = (By.XPATH, "//div[@class='broadcast_top']/div[2]/span[2]/a")
    listen_number_loc = (By.XPATH, "//div[@class='broadcast_top']/div[2]/span[4]/a")
    audience_number_loc = (By.XPATH, "//div[@class='broadcast_top']/div[2]/span[6]/a")

    # 广播数
    def broadcast_number(self):
        return self.find_element(*self.broadcast_number_loc).text

    # 收听数
    def listen_number(self):
        return self.find_element(*self.listen_number_loc).text

    # 听众数
    def audience_number(self):
        return self.find_element(*self.audience_number_loc).text

    dynamic_input_loc = (By.ID, "fastpostmessage")
    publish_button_loc = (By.ID, "fastpostsubmit")
    new_dynamic_loc = (By.XPATH, "//ul[@id='followlist']/li[1]/div/div[2]/div[2]")

    # 动态输入框
    def dyamic_input(self, info):
        self.find_element(*self.dynamic_input_loc).send_keys(info)

    # 发表按钮
    def publish_button(self):
        self.find_element(*self.publish_button_loc).click()

    # 最新发送的一条广播
    def new_dynamic(self):
        return self.find_element(*self.new_dynamic_loc).text

    new_rebroadcast_loc = (By.CLASS_NAME, "y")
    new_rebroadcast_input_loc = (By.XPATH, "//span[@class='flw_autopt']/textarea")
    new_rebroadcast_button_loc = (By.ID, "relaysubmit_btn")

    # 点击"转播"展开输入框
    def new_rebroadcast(self):
        self.find_element(*self.new_rebroadcast_loc).pop(1).click()

    # 转播输入框
    def new_rebroadcast_input(self, value):
        self.find_element(*self.new_rebroadcast_input_loc).send_keys(value)

    # 转播按钮
    def new_rebroadcast_button(self):
        self.find_element(*self.new_rebroadcast_button_loc).click()

    new_reply_loc = (By.XPATH, u"//ul[@id='followlist']/li[1]/div/div[2]/div[3]/div/span/a[2]")
    new_reply_input_loc = (By.XPATH, "//span[@class='flw_autopt']/textarea")
    new_reply_button_loc = (By.ID, "postsubmit")

    # 点击“回复”展开输入框
    def new_reply(self):
        aa = self.driver.find_elements_by_tag_name("a")
        for a in aa:
            if a.text == "回复 ":
                a.click()
                break
        else:
            print
            "time out! not find reply button"

    # 回复输入框
    def new_reply_input(self, value):
        self.find_element(*self.new_reply_input_loc).send_keys(value)

    # 回复按钮
    def new_reply_button(self):
        self.find_element(*self.new_reply_button_loc).click()

    new_delete_button_loc = (By.XPATH, "//ul[@id='followlist']/li[1]/div/div[2]/a")
    new_delete_button_display_loc = (By.XPATH, "//ul[@id='followlist']/li[1]")
    new_delete_true_loc = (By.NAME, "btnsubmit")
    new_delete_info_loc = (By.XPATH, "//div[@class='alert_right']/p")

    # 点击删除的小图标
    def new_delete_button(self):
        self.driver.refresh()
        for i in range(10):
            try:
                above = self.find_element(*self.new_delete_button_loc)
                ActionChains(self.driver).move_to_element(above).perform()
                sleep(0.5)
                display = self.find_element(*self.new_delete_button_display_loc).get_attribute('class')
                if "flw_feed_hover" in display:
                    above.click()
                    break
            except:
                pass
            self.driver.refresh()
        else:
            print
            "time out! not find delete button"

    # 删除确认按钮
    def new_delete_ture(self):
        self.find_element(*self.new_delete_true_loc).click()
        sleep(1)

    # 删除成功的提示信息
    def new_delete_info(self):
        return self.find_element(*self.new_delete_info_loc).text

    '''
    我的动态--大厅标签页 
    '''
    hall_loc = (By.XPATH, "//div[@class='page_frame_navigation']/ul/li[2]/a")

    def hall(self):
        self.find_element(*self.hall_loc).click()

    '''
    我的动态--广播标签页 
    '''
    broadcast_loc = (By.XPATH, "//div[@class='page_frame_navigation']/ul/li[3]/a")

    def broadcast(self):
        self.find_element(*self.broadcast_loc).click()


if __name__ == '__main__':
    pass


