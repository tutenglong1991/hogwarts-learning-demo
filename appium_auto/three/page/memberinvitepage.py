#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium_auto.three.page.ContactAddPage import ContactAddPage
from appium_auto.three.page.base_page import BasePage

class MemberInvitePage(BasePage):
    pass

    def click_menualadd(self):
        return ContactAddPage(self._driver)

    def click_back(self):
        from appium_auto.three.page.addresslistpage import AddressListPage
        return AddressListPage(self._driver)