import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

# 1. GET
res_get = requests.get(f"{base_url}/1")
print("GET status:", res_get.status_code)

# 2. POST
res_post = requests.post(base_url, json={"title": "Yangi post", "body": "Matn", "userId": 1})
print("POST status:", res_post.status_code, "| Yaratilgan ID:", res_post.json().get("id"))

# 3. PUT
res_put = requests.put(f"{base_url}/1", json={"title": "Yangilangan post", "body": "Yangi matn", "userId": 1})
print("PUT status:", res_put.status_code)

# 4. DELETE
res_delete = requests.delete(f"{base_url}/1")
print("DELETE status:", res_delete.status_code)
