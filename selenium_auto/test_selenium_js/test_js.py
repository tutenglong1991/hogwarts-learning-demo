#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium_auto.test_windows_and_frame_locate.Base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        time.sleep(3)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(code)
            print(self.driver.execute_script(code))



