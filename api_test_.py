import requests

# 访问百度（国内网站，保证不超时）
url = "https://www.baidu.com"
response = requests.get(url)

print("状态码:", response.status_code)   # 预期看到 200
print("返回内容前100个字符:")
print(response.text[:100])