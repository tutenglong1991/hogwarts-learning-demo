#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pytest


class TestRequestsDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.text)
        # print(r.json())
        assert r.status_code == 200

    # Get Query请求
    def test_query(self):
        payload={
            "level":1,
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    # Form请求参数构造
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    # 文件上传
    # files = {'file': open('report.xls', 'rb')}
    # r = requests.post(url, files=files)
    # def test_files_post(self):
    #     r = requests.post(url="", files="")
    #     print(r.text)

    # header和cookis处理
        # headers = {'user-agent': 'my-app/0.01'}
        # r = requests.get(url, headers=headers)
    # cookie
        # cookies = dict(cookies_are='working')
        # r = requests.get(url. cookies=cookies)
    def test_header(self):
        r = requests.get("https://httpbin.testing-studio.com/get", headers={"h": "header demo"})
        print(r.text)
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "header demo"


if __name__ == '__main__':
    pytest.main('-v', '-s', "test_request_method.py")
