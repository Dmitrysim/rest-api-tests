import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parse_response_text = response.json()
print(parse_response_text["answer"])
print(response.status_code)

response2 = requests.get("https://playground.learnqa.ru/api/check_type", params=payload)
print(response2.text)

# В post, delete, patch тип будет data

response3 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1", "value1"})
print(response3.text)

headers = {"some_header":"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

print(response.text)

payload1 = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload1)

print(response1.text)
print(response1.status_code)
print(dict(response1.cookies))
print()

cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie':cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response2.text)


