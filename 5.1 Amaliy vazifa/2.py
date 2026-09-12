import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Yangilangan sarlavha",
    "body": "Post matni mazmuni",
    "userId": 1
}

response = requests.post(url, json=data)
print("Status kodi:", response.status_code)
if response.status_code in [200, 201]:
    print("Resurs muvaffaqiyatli yaratildi:", response.json())
