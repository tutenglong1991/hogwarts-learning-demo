#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# fixture中添加autouse=True参数，模块或类中其他方法没有将
# 被修饰的方法作为参数传入，也会在执行前自动执行被修饰的方法
@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")


def test_search1():
    print("test_search1")
    pass


def test_search2():
    print("test_search2")


def test_search3():
    print("test_search3")