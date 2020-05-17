#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
场景：你已经可以将测试方法前要执行的或依赖的解决了，测试方法后销毁清除数据的要如何进行呢？范围是模块级的。类似setupClass
解决：通过在同一模块中加入yield关键字，yield是调用第一次返回结果，第二次执行它下面的语句返回
步骤： 在@pytest.fixture(scope=module)
在登录的方法中加入yield，之后加销毁清除的步骤，注意这种方式没有返回值，如果希望返回使用addfinalizer
"""
import pytest


# 作用域：module是在模块前后执行的
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown ！")
    print("最后关闭浏览器")


def test_search1(open):
    print("test_search1")
    pass


def test_search2():
    print("test_search2")


def test_search3():
    print("test_search3")


"""
def setup_module():
    print("打开浏览器")


def teardown_module():
    print("执行teardown ！")
    print("最后关闭浏览器")


def test_search1():
    print("test_search1")
    pass


def test_search2():
    print("test_search2")
"""

if __name__ == '__main__':
    pytest.main()
