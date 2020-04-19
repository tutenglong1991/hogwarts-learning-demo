#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium_auto.three.page.base_page import BasePage
# from appium_auto.three.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):

    def click_addmember(self):
        from appium_auto.three.page.memberinvitepage import MemberInvitePage
        return MemberInvitePage(self._driver)

