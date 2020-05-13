#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from appium_auto.three.page.app import App


class TestAddContact():
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize("username, gender, phonenum", yaml.save)
    def test_addcontact(self):
        self.main.goto_addresslist().\
            click_

