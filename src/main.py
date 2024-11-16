import requests
import json

def get(url):
    # get 请求
    req = requests.get(url)
    # 输出状态码
    print(req.status_code)
    # 输出返回内容
    print(req.text)

def post(url):
    # post 参数
    post_data = ""
    # post 请求头
    headers = ""

    req = requests.post(url, data=post_data, headers=headers)

    data = json.loads(req.text)

    print(req.status_code)
    print(req.text)

if __name__ == '__main__':
    phone_number = "13467025014"

    post("https://n.cg.163.com/api/v1/phone-captchas/86-13467025014")