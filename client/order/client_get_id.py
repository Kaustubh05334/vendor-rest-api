import requests

order_id=input("Enter the id: ")
url = f"http://127.0.0.1:8000/api/purchase_orders/{order_id}/"
response = requests.get(url)
print(response.text)