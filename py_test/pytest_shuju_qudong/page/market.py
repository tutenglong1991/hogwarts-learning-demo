from appium_auto.three.page.base_page import BasePage
from py_test.pytest_shuju_qudong.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)