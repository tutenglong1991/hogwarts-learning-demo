#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import yaml
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy


class BasePage:

    _black_list = [
        (MobileBy.XPATH, "//*[]@text='确定"),
        (MobileBy.XPATH, "//*[]@text='允许"),
        (MobileBy.XPATH, "//*[]@text='确定")
    ]
    _error_num = 0
    _error_max = 3
    _param = {}
    logging.basicConfig(level=logging.INFO)

    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self, locator, value):
        logging.info(locator)
        try:
            return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
        except Exception as e:
            if self._error_num > self._error_max:
                raise e
            self._error_num += 1
            # 处理弹框
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    self.find(locator, value)

    def steps(self, file):
        with open(file) as f:
            steps:List[dict] = yaml.safe_load()
            element:WebElement
            for step in steps:
                if 'by' in step.keys():
                    myby = step['by']
                    if myby == 'id':
                        element = self.find(step['by'], step['locator'])
                    if myby == 'xpath'
                        element = self.find(MobileBy.XPATH, step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'find':
                        pass
                    elif action == 'click':
                        element.click()
                    elif action == 'send':
                        pass
