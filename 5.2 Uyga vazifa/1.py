import requests

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("--- O'zbekiston Markaziy Banki Valyuta Kurslari ---")
    for currency in data[:5]:
        print(f"Valyuta: {currency['Ccy']} ({currency['CcyNm_UZ']}) | Kurs: {currency['Rate']} so'm | Sana: {currency['Date']}")
