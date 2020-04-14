#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium_auto.test_windows_and_frame_locate.Base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle) # 跳转前打印当前窗口
        print(self.driver.window_handles) # 打印所有窗口
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle) # 跳转后打印当前窗口
        print(self.driver.window_handles) # 打印所有窗口
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        print(self.driver.current_window_handle) # 使用switch_to_window转换当前的窗口为跳转后的窗口再打印当前窗口
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13570808795")
        time.sleep(2)
        self.driver.switch_to_window(windows[0])
        time.sleep(2)
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()


