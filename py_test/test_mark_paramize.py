#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# pytest.mark.parametrize 支持用例参数化，该方法接收参数形式如：
# pytest.mark.parametrize("3+5->test_input, 8->expected", [("表达式", expected), ()...])

@pytest.mark.parametrize("test_input1, expected", [("3+5", 8), ("2*5", 10), ("5%2", 1)])
def test_eval(test_input1, expected):
    # eval将字符串str当成有效的表达式来求值，并返回结果
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


@pytest.mark.skip("次测试不执行登陆")
# indirect=True, 可以把传过来的参数当做函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""


if __name__ == '__main__':
    pytest.main("-v")

