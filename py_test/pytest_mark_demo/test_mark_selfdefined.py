#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
----使用自定义标记mark只执行某部分用例----
场景
    只执行符合要求的某一部分用例，可以把一个项目划分为多个模块，然后指定模块名称执行
    App自动化时，如果想Android和ios公用一套代码时，也可以使用标记功能，表明哪些是ios的用例，哪些是Android，运行代码时指定mark名称运行就可以。
解决
    在测试用例方法上加@pytest.mark.webtest
执行：
    -s参数：输出所有测试用的print信息
    -m: 执行自定义标记的相关用例pytest -s test_mark_selfdefined.py
        pytest -s test_mark_selfdefined.py -m pc
        pytest -s test_mark_selfdefined.py -m app
        pytest -s test_mark_selfdefined.py -m ios
"""
import pytest

@pytest.mark.search
def test_search1():
    print("test_search1")
    raise NameError
    pass

@pytest.mark.search
def test_search2():
    print("test_search2")
    pass

@pytest.mark.search
def test_search3():
    print("test_search3")
    pass

@pytest.mark.login
def test_login1():
    print("test_login1")
    pass

@pytest.mark.login
def test_login2():
    print("test_login2")
    pass


if __name__ == '__main__':
    pytest.main()