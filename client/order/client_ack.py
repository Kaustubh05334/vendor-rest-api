import requests

po_id = input("Enter Purchase order id: ")
url = f"http://127.0.0.1:8000/api/purchase_orders/{po_id}/acknowledge/"
data = {
    "acknowledgment_date":"2021-9-10T00:00:00Z",
}
response = requests.post(url,json=data)
print(response)
