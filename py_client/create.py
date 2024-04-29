import requests


#Django Server 
endpoint = "http://localhost:8000/api/products/"

data={
    "title":"This feild is more",
    "price":"312"
}
get_response = requests.post(endpoint, json=data)


print(get_response.json())