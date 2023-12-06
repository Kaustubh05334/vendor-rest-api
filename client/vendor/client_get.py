import requests



url = "http://127.0.0.1:8000/api/vendors/"
response = requests.get(url)
print(response.json())
