import requests

endpoint ="http://127.0.0.1:8000/api/"
#endpoint="https://httpbin.org/anything"

get_response = requests.get(endpoint, params={"abcd":1234}, json = {"query":"hello world"})
print(get_response.text)
# print(get_response.json())

print(get_response.status_code)