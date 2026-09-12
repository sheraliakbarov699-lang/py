import requests
import time

url = "https://httpbin.org/status/500,200"  # Test uchun manzil
max_retries = 3
delay = 2

for attempt in range(1, max_retries + 1):
    try:
        print(f"{attempt}-urinish yuborilmoqda...")
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if response.status_code == 200:
            print("So'rov muvaffaqiyatli bajarildi!")
            break
    except requests.RequestException as e:
        print(f"Tarmoq xatosi: {e}")
    
    if attempt < max_retries:
        print(f"{delay} soniya kutilmoqda...")
        time.sleep(delay)
else:
    print("Barcha 3 marta urinish muvaffaqiyatsiz tugadi.")
