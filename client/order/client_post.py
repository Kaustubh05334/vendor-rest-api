import requests

url = "http://127.0.0.1:8000/api/purchase_orders/"
data = {
    "vendor_id": 1,
    "po_number": "12326212",
    "order_date": "2021-01-01T00:00:00Z",
    "delivery_date": "2021-12-10T00:00:00Z",
    "items": {"item1": "description", "item2": "description"},
    "quantity": 10,
    "status": "completed",
    "quality_rating": 2.5,
    "issue_date": "2021-01-01T00:00:00Z",
    "acknowledgment_date":"2021-10-10T00:00:00Z",
}
response = requests.post(url,json=data)
print(response)