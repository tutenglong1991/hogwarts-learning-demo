#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jsonpath
import pytest
import requests


class TestJsonPath:

    # 传统的根据python数据类型解析
    def test_hogwarts_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'

    # 使用jsonpath解析
    def test_hogwarts_jsonpath(self):
        url = "https://home.testing-studio.com/categories.json"
        r = requests.get(url)
        # print(JsonPath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'


if __name__ == '__main__':
    pytest.main('-v', '-s', "test_request_jsonpath.py")
