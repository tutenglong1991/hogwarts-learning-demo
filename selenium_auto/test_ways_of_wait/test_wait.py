#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sleep 强制等待，缺点是对设置的时间参数不同场景不好把握
# implicitly_wait 隐式等待，缺点是设置对全局生效，若查找元素失败后会一直进行查找，知道超过设置的等待时间
# WebDriverWait 显示等待，通过until和until_not自定义等待条件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        # self.driver.implicitly_wait(5)

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]').click()
        # self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
        # def wait(x): # 该函数一定更要有一个参数
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]'))
        # WebDriverWait(self.driver, 5).until(wait)# 这里不能写成()，括号表示函数调用，不是传参
        WebDriverWait(self.driver, 4).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))