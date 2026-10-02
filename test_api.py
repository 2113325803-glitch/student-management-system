import requests

def test_get_baidu():
    """测试百度首页接口，断言状态码为200"""
    url = "https://www.baidu.com"
    response = requests.get(url)               #GET：向服务器“要”数据，参数挂载URL后面

    assert response.status_code == 200            #POST: 向服务器“送”数据，参数藏在请求体boby中


def test_post_json():
    """测试：发送 POST 请求，提交 JSON 数据"""
    url = "https://httpbin.org/post"
    payload = {
        "username": "admin",
        "password": "123456"
    }
    # 发送 POST 请求，json=payload 会自动把字典转成 JSON 字符串，并加上 Content-Type: application/json
    response = requests.post(url, json=payload)

    # 断言：状态码 200，且返回的 JSON 里包含了我们提交的数据
    assert response.status_code == 200
    data = response.json()
    assert data["json"]["username"] == "admin"
    assert data["json"]["password"] == "123456"


def test_post_with_token():
    """测试：模拟携带 Token 鉴权访问接口"""
    url = "https://httpbin.org/post"
    # 1. 自定义请求头（模拟登录后服务器发给我们的 Token）
    headers = {
        "Authorization": "Bearer my_secret_token_123456",
        "Content-Type": "application/json"
    }
    payload = {"action": "get_student_list"}

    # 2. 发送请求，带上 headers
    response = requests.post(url, json=payload, headers=headers)

    # 3. 断言：状态码 200，且服务器确认收到了我们的 Token
    assert response.status_code == 200
    data = response.json()
    assert "Authorization" in data["headers"]
    assert data["headers"]["Authorization"] == "Bearer my_secret_token_123456"