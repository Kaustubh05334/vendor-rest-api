import requests


vendor_id = input("Enter vendor id: ")
url = f'http://127.0.0.1:8000/api/vendors/{vendor_id}/performance'

response = requests.get(url)

print(response.json())