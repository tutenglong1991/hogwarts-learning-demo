#!/usr/bin/env python
# -*- coding: utf-8 -*-
# frame存在两种：
# 一种是嵌套的，一种是为嵌套的

# 切换frame
# driver.switch_to.frame() 根据元素id或者index切换frame，无id时使用索引，索引从0开始
# driver.switch_to.default_content() 切换到默认的frame
# driver.switch_to.parent_frame() # 切换到父级frame

# 注意嵌套处理
# 需要先切换到父节点frame，再切换到子节点，处理完之后再切回父节点，一层一层处理
from selenium_auto.test_windows_and_frame_locate.Base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("http://runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()  # 切回父节点
        # self.driver.switch_to.defalut_content() # 切回默认节点，即首次打开节点
        print(self.driver.find_element_by_id("submitBTN").text)
