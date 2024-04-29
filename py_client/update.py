import requests


#Django Server 
endpoint = "http://localhost:8000/api/products/1/update/"

data={
    "title": "my new hello",
    "price": 323
}

get_response = requests.put(endpoint,json=data)


print(get_response.json())