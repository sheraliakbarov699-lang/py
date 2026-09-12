import json

config = {
    "env": "production",
    "port": 8080,
    "debug": False
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("JSON fayldan o'qilgan konfiguratsiya:", data)
