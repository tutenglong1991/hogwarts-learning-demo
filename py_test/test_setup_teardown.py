#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 模块级（setup_module、teardowm_module）模块始末，全局的（优先级最高）
# 函数级（setup_function/teardown_function）只对模块中的函数（不包括类中的）用例生效
# 类级（setup_class/teardown_class）只在类中前后运行一次（在类中）
# 方法级（setup_method/teardown_method）开始于方法始末（在类中）
# 类里面的（setup/teardown）运行在调用方法的前后
# 需要注意不同级别的setup*和teardown*要成对出现

import pytest


def setup_module():
    print("这是模块级的setup_module方法：setup_module")


def teardown_module():
    print("这是模块级的teardown_module方法：teardown_module")


def setup_function():
    print("这是模块中，类外面的方法执行前执行的：setup_function")


def teardown_function():
    print("这是模块中，类外面方法执行后执行的：teardown_function")


def test_login():
    print("正在执行模块中，类外面的函数...........")


# 测试类必须是T大写的Test标识
class TestDemo2:
    def setup_class(self):
        print("类被实例化或执行前执行的内容：setup_class")

    def setup_method(self):
        print("类里面的方法执行前执行的：setup_method")

    def setup(self):
        print("setup")

    def teardown_method(self):
        print("类里面的方法执行后执行的：teardown_method")

    def teardown(self):
        print("teardown")

    def teardown_class(self):
        print("类被实例化或执行后执行的内容：teardown_class")

    # 测试方法需要已test单词开头或结尾的：test_*, *_test
    def test_class_inner_method(self):
        print("这在执行类中的方法........")


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_setup_teardown.py'])
