import requests

vendor_id = input("Enter a valid id: ")
url= f"http://127.0.0.1:8000/api/vendors/{vendor_id}/"
response = requests.delete(url)
print(response)
