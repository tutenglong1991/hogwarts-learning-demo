from appium.webdriver import webdriver
from appium_auto.three.page.main import Main
from py_test.pytest_shuju_qudong.page.base_page import BasePage


class App(BasePage):
    def start(self):
        _package="com.xueqiu.android"
        _activity=".view.WelcomeActivityAlias"
        if self._driver is None:
            caps=dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "package"
            caps["appActivity"] = "activity"
            caps["autoGrantPermissions"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicity_wait(3)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)
