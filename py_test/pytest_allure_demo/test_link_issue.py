#!/usr/bin/env python
# -*- coding: utf-8 -*-

import allure


@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass


TEST_CASE_LINK = 'http://www.baidu.com'


@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase():
    print("这是一条测试用例的链接， 链接到测试用例管理工具中详细用例说明页")
    pass


# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}，该修饰符可用例管理缺陷，140即为bug管理平台中对应的id值
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass
