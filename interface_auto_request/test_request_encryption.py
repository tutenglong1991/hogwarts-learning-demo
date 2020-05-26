import json

import pytest
import requests
import base64


class TestRequestEncode:

    def send(self, data: dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            res_json = json.loads(base64.b64decode(res.content))  # r.content将返回流转换成二进制
            return res_json
        elif data["encoding"] == "private":
            # 把加密过后的响应值发给第三方服务，让第三方服务做解密后返回解密过后的信息
            return requests.post("url", data=res.content)

    def test_encode_send(self):
        req_data = {
            "method": "get",
            "url": "http://127.0.0.1:9999/demo.txt",
            "headers": None,
            "encoding": "base64"
        }
        print(self.send(req_data))


if __name__ == "__main__":
    pytest.main('-v', '-s', "test_request_encryption.py")
