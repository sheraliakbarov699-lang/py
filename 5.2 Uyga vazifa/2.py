import requests

# requests.Session() TCP ulanishni (connection pooling) qayta ishlatadi.
# Bu bir nechta so'rov yuborilganda tezlikni oshiradi va server bilan qayta ulanish vaqtini tejaydi.

session = requests.Session()
session.headers.update({"User-Agent": "MyApp/1.0"})

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

print("Session orqali so'rovlar yuborilmoqda:")
for url in urls:
    res = session.get(url)
    print(f"Status: {res.status_code} | Title: {res.json().get('title')[:20]}...")
