import requests

url = "http://127.0.0.1:8000/api/purchase_orders/"

response = requests.get(url)
print(response)