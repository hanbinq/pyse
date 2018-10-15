class Page(object):
    """
    基本类，用于所有页面的继承
    """

    login_url = "http://bbs.meizu.cn"

    def __init__(self, selenium_driver, base_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def script(self, src):
        return self.driver.execute_script(src)

