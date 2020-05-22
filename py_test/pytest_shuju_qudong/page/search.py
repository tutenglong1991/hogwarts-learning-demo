from appium_auto.three.page.base_page import BasePage
from py_test.pytest_shuju_qudong.page.market import Market


class Search(BasePage):
    def search(self, value):
        self._param["value"]=value
        self.steps("../page/search.yaml")
        return Market(self._driver)