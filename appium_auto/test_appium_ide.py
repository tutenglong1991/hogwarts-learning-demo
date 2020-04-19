#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver
desire_cap = {
    "platformName": "android",
    "devicesName": "emulator-5554",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "onRest": True # onRest可避免app数据被重置，如可避免重复弹出登陆更新等弹窗等，可记录登陆状态
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(5)