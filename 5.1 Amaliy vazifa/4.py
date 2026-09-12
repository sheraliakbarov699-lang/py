import requests

def check_response_status(status_code):
    if status_code == 200:
        print("200 OK: So'rov muvaffaqiyatli bajarildi!")
    elif status_code == 404:
        print("404 Not Found: So'ralgan resurs topilmadi!")
    elif status_code == 500:
        print("500 Internal Server Error: Server ichki xatoligi!")
    else:
        print(f"Boshqa status kodi: {status_code}")

# Test qilish
check_response_status(200)
check_response_status(404)
check_response_status(500)
