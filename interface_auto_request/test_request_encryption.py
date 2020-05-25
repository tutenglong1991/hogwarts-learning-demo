import json
import requests
import base64


def test_encode():
    url = "http://127.0.0.1:9999/demo.txt"
    r = requests.get(url=url)
    res_json = json.loads(base64.b64decode(r.content))  # r.content将返回流转换成二进制
    print(res_json)
