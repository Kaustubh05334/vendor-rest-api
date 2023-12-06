import requests

order_id = input("Enter the number: ")
url = f"http://127.0.0.1:8000/api/purchase_orders/{order_id}/"
data = {
    "vendor_id": 1,
    "po_number": "12345678",
    "order_date": "2021-01-01T00:00:00Z",
    "delivery_date": "2021-11-10T00:00:00Z",
    "items": {"item1": "description", "item2": "description"},
    "quantity": 10,
    "status": "completed",
    "quality_rating": 4.5,
    "issue_date": "2021-01-01T00:00:00Z",
    "acknowledgment_date":"2021-10-10T00:00:00Z",
}
response = requests.put(url,json=data)
print(response)