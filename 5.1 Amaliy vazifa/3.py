import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Authorization": "Bearer my_secret_test_token_12345",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print("Sarlavhalar bilan yuborilgan so'rov statusi:", response.status_code)
