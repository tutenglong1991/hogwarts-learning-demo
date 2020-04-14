#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest


def test_02():
    print('我是文件中的测试用例02')
    x = 'this'
    assert 'h' in x


class TestDemo:
    # 测试类不能有init方法
    def test_03(self):
        print('我是TestDemo类中的测试用例03')
        x = 'hello'
        # assert 'e' in x
        pytest.assume('h' not in x)
        pytest.assume('x' in 'xxxx')

    def test_04(self):
        print('我是TestDemo类中的测试用例04')
        a = 'hello'
        b = 'hello world'
        assert a in b


class TestDemo1:
    # 测试类不能有init方法
    def test_05(self):
        print('我是TestDemo1类中的测试用例03')
        x = 'hello'
        assert 'e' in x

    def test_06(self):
        print('我是TestDemo1类中的测试用例04')
        a = 'hello'
        b = 'hello world'
        assert a in b


if __name__ == '__main__':
    pytest.main(["-v", "-x", "test_begin.py"])
    # pytest.main(['-v', '-s', 'TestDemo1'])
    # pytest.main()
