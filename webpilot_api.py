import requests

url = 'https://preview.webpilotai.com/api/v1/watt'
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer <YOUR API-KEY>'  # 注意：令牌不需要尖括号
}
data = {
    #<WEBSITE YOU WANT TO CONCLUDE> is not a must
    "content": "<YOUR QUESTION>?<WEBSITE YOU WANT TO CONCLUDE>"
}

response = requests.post(url, headers=headers, json=data)

print("响应状态码:", response.status_code)
print("响应内容:", response.text)
