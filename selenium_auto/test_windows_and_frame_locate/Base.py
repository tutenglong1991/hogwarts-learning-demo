#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver


class Base:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self):
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()  # 放大浏览器

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
