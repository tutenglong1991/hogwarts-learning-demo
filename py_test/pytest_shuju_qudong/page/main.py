from appium_auto.three.page.base_page import BasePage
from py_test.pytest_shuju_qudong.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)
