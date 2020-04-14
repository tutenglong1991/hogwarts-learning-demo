#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
该类为公共方法类，使用pytest.fixture注解表示，
后续方法可使用里面函数名作为参数化调用
1.文件名不能换的；
2.conftest与运行的用例要在同一个package下，即要有__init__文件
3.不需要import导入conftest.py,pytest用例会自动查找
4.全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包下数据全局共享
"""
import pytest


# 不带参数的fixture默认参数为 scope=function
@pytest.fixture()
def login():
    print("这是个登录方法")


def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签集合
    for makers in marker_list:
        config.addinivalue_line(
            "markers", makers
        )
