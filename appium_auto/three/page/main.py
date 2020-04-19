#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium_auto.three.page.addresslistpage import AddressListPage
from appium_auto.three.page.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addresslist(self):
        self.steps1("../steps/mainsteps.yml")
        return AddressListPage(self._driver)

    def goto_workbench(self):
        pass
