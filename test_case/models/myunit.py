import unittest, time
import driver


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = driver.browser()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':

    class Test(MyTest):

        def test_case(self):
            self.driver.get("http://www.baidu.com")
            self.driver.find_element_by_id("kw").send_keys("unittest")

    unittest.main()


