#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# pytest.mark.parametrize 支持用例参数化，该方法接收参数形式如：
# pytest.mark.parametrize("3+5->test_input, 8->expected", [("表达式", expected), ()...])
import sys


@pytest.mark.parametrize("test_input1, expected", [("3+5", 8), ("2*5", 10), ("5%2", 1)])
def test_eval(test_input1, expected):
    # eval将字符串str当成有效的表达式来求值，如将"3+5",转成（3+5）算数表达式，并返回结果
    assert eval(test_input1) == expected


# 参数组合
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x:{x}, y:{y}")


# 方法名作为参数
test_user_data = ['Tome', 'Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    # 这是接收并传入的参数
    user = request.param
    print(f"\n 打开首页准备登陆， 登陆用户：{user}")
    return user

# indirect=True, 可以把传过来的参数当做函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login1(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""


"""
Skip 使用场景
    调试时不想运行这个用例
    标记无法在某些平台上运行的测试功能
    在某些版本中执行，其他版本中跳过
    当前的外部资源不可用是跳过（如测试数据从数据库获取，数据库连接失败，或者依赖前置服务调用失败等）
解决：
    @pytest.mark.skip跳过这个测试用例，可以加skipif，在满足某些条件下才希望通过，否则跳过这个测试

Xfail场景
    功能测试尚未实施或尚未修复的错误，当测试通过时尽管预计会失败（标记为@pytest.mark.xfail），它是一个xpass，将在测试摘要中报告
    你希望由于某种情况而就应该失败
解决：
    @pytest.mark.xfail
"""
@pytest.mark.skipif(sys.platform == "win32", reason="不在windows上执行")
# @pytest.mark.skip("次测试不执行登陆")
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login2(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""

@pytest.mark.xfail
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login3(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""


if __name__ == '__main__':
    pytest.main("-v")

