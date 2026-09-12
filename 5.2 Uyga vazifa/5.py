import os
import requests

# API token kod ichida emas, muhit o'zgaruvchisidan olinadi
api_token = os.environ.get("MY_API_TOKEN", "default_test_token")

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

url = "https://jsonplaceholder.typicode.com/headers"
response = requests.get(url, headers=headers)

print("Xavfsiz so'rov statusi:", response.status_code)
print("Ishlatilgan token:", api_token[:4] + "****")
