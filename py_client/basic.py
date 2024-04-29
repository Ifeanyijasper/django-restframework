import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

#Django Server 
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello World"})
# print(get_response.text)
# print(get_response.status_code)

#JSON

print(get_response.json())