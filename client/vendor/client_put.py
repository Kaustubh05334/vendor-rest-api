import requests

vendor_id = input("Enter a valid id: ")
data = {
    "name": "ABC Ventures Updated",
    "contact_details": "contact@abcventures.com",
    "address": "New Address, Udaipur, Rajasthan, India",
    "vendor_code": "11111111",
}
response = requests.put(f"http://127.0.0.1:8000/api/vendors/{vendor_id}/", json=data)
print(response)
