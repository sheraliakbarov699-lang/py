# 1-topshiriq: Listdagi juft sonlarni ajratuvchi funksiya
def juft_sonlarni_ajrat(sonlar):
    return [x for x in sonlar if x % 2 == 0]

# 2-topshiriq: Server va IP lardan iborat dict va uning kalit-qiymatlari
servers = {
    "web-server": "192.168.1.10",
    "db-server": "192.168.1.20",
    "cache-server": "192.168.1.30"
}
def print_servers():
    for name, ip in servers.items():
        print(f"Server: {name} -> IP: {ip}")

# 3-topshiriq: 1 dan 100 gacha bo'lgan sonlar yig'indisini for tsikli bilan hisoblash
def sum_1_to_100():
    total = 0
    for i in range(1, 101):
        total += i
    return total

# 4-topshiriq: Foydalanuvchidan int so'rash va try/except qo'llash
def get_integer_input():
    user_input = input("Butun son kiriting: ")
    try:
        val = int(user_input)
        print(f"Rahmat, siz kiritgan son: {val}")
    except ValueError:
        print("Xatolik: Kiritilgan qiymat butun son emas!")

# 5-topshiriq: Ikki sonni bo'lish va ZeroDivisionError ushlash
def safe_divide(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print("Xatolik: Nolga bo'lish mumkin emas!")
        return None

if __name__ == "__main__":
    print("--- 2.1 AMALIY VAZIFA ---")
    print("1. Juft sonlar:", juft_sonlarni_ajrat([1, 2, 3, 4, 5, 6, 7, 8]))
    print("\n2. Serverlar ro'yxati:")
    print_servers()
    print("\n3. 1 dan 100 gacha yig'indi:", sum_1_to_100())
    print("\n5. Bo'lish testi (10 / 0):")
    safe_divide(10, 0)
