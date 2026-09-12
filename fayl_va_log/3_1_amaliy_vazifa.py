import json
import yaml
import csv
import logging

# 1-topshiriq: Matnli faylga with open() bilan 5 qator log qo'shish
with open("app.log", "a") as f:
    for i in range(1, 6):
        f.write(f"Log yozuvi qatori #{i}\n")

# 2-topshiriq: JSON faylda konfiguratsiyani saqlash va o'qish
config_data = {"env": "development", "port": 8080, "debug": True}
with open("config.json", "w") as f:
    json.dump(config_data, f, indent=4)

with open("config.json", "r") as f:
    read_config = json.load(f)
    print("JSON Config:", read_config)

# 3-topshiriq: YAML formatida server ro'yxatini yozish va o'qish
servers_yaml = {
    "servers": [
        {"name": "web-01", "ip": "10.0.0.1"},
        {"name": "db-01", "ip": "10.0.0.2"}
    ]
}
with open("servers.yaml", "w") as f:
    yaml.dump(servers_yaml, f)

with open("servers.yaml", "r") as f:
    read_yaml = yaml.safe_load(f)
    print("YAML Serverlar:", read_yaml)

# 4-topshiriq: CSV faylga xodimlar ma'lumotini yozish va jadval ko'rinishida chiqarish
employees = [
    ["ID", "Ism", "Lavozim"],
    [1, "Ali", "DevOps Engineer"],
    [2, "Vali", "Python Developer"],
    [3, "Sami", "System Administrator"]
]
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

print("\n--- CSV Xodimlar Jadvali ---")
with open("employees.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row[0]:<5} | {row[1]:<10} | {row[2]:<20}")

# 5-topshiriq: logging moduli yordamida voqealarni faylga yozish
logging.basicConfig(filename="script_events.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Skript ishlashi START bo'ldi")
try:
    res = 10 / 0
except Exception as e:
    logging.error(f"Xatolik yuz berdi: {e}")

logging.info("Skript ishlashi TUGADI")
print("\n3.1 Amaliy vazifa barcha topshiriqlari bajarildi.")
