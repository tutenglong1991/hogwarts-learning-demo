#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium_auto.three.page.base_page import BasePage
from appium_auto.three.page.main import Main


class App(BasePage):
    # 启动app初始化父类的driver
    def start(self):
        caps = {}
        caps["devicesName"] = ""
        caps["activity"] = ""
        self._driver = Webdriver.
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)