#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用allure生成报告：
1.根据不同运行平台或语言先安装allure，参照官方文档；
2.使用--alluredir参数指定结果数据存放目录，如：pytest test_allure_demo1.py --alluredir=./result/5
3.通过allure serve ./result/5(测试结果存放目录)会直接打开默认浏览器战士当前报告,注意需要先去官网下载allure安装包直接解压，放到环境变量中才能执行该命令
4.从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告，打开报告
  .生成报告
     allure generate ./result/ -o ./report/ --clear(注意：覆盖路径加--clear)
  .打开报告
     allure open -h 127.0.0.1 -p 8883 ./report/
"""
import allure
import pytest


# feature修饰，可在执行时通过--allure-features '模块名称'，如本例中的【登录模块】，或--allure-stories '用例名称'即story中的入参
# 指定需执行的模块用例，需要注意windows系统上此处若出现提示模块名或名称找不到，命令行中模块名不要加引号或直接--allure-features=模块名
@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录测试用例，登录成功")
        pass

    @allure.story("登录失败，用户名缺失")
    def test_login_failure_no_username(self):
        print("这是登录测试用例，无用户名")
        pass

    @allure.story("登录失败，密码缺失")
    def test_login_failure_no_password(self):
        # step用法可在报告中显示出详细步骤，参数为步骤说明
        with allure.step("点击用户名输入框"):
            print("输入用户名")
        with allure.step("点击密码输入框"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass


@allure.feature("搜索模块")
class TestSearch:
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录测试用例，登录成功")
        pass

    @allure.story("登录失败，用户名缺失")
    def test_login_failure_no_username(self):
        print("这是登录测试用例，无用户名")
        pass

    @allure.story("登录失败，密码缺失")
    def test_login_failure_no_password(self):
        # step用法可在报告中显示出详细步骤，参数为步骤说明
        with allure.step("点击用户名输入框"):
            print("输入用户名")
        with allure.step("点击密码输入框"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登录失败")
        pass


if __name__ == '__main__':
    pytest.main()
