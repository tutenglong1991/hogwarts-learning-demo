#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
一、多线程并行执行：
    pytest分布式执行插件：pytest-xdist，多个CPU或主机执行，前提：
    用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不
    影响其他用例
    pip install pytest-xdist
    多个CPU并行执行用例，直接加-n，3是并行数量：pytest -n 3

二、使用pytest-html模块生成测试报告：
 1、pip install pytest-html
 2、进入需要生成测试报告或执行了的用例目录，输入命令：pytest -v -s --html=report.html --self-contained-html

"""
def test_case1():
    print("test_case1, 需要登录")
    pass


def test_case2():
    print("test_case2, 不需要登录")
    pass


def test_case3():
    print("test_case3, 需要登录")
    pass

def test_case3():
    print("test_case3, 需要登录")
    pass

def test_case4():
    print("test_case3, 需要登录")
    pass

def test_case5():
    print("test_case3, 需要登录")
    pass

def test_case6():
    print("test_case3, 需要登录")
    pass

def test_case7():
    print("test_case3, 需要登录")
    pass

def test_case8():
    print("test_case3, 需要登录")
    pass

def test_case9():
    print("test_case3, 需要登录")
    pass
def test_case10():
    print("test_case3, 需要登录")
    pass