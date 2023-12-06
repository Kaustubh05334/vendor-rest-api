import requests


url = "http://127.0.0.1:8000/api/vendors/"
data= {
    "name":"ABD Ventures",
    "contact_details":"abd.ventures@gmail.com",
    "address":"x20kk,Block Street,Udaipur,Rajasthan,India",
    "vendor_code":"11111161",
}
response = requests.post(url,json=data)
print(response)