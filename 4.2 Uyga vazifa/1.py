import os

# Qo'lda .env faylini yaratish hamda o'qish
with open(".env", "w", encoding="utf-8") as f:
    f.write("DB_HOST=localhost\nDB_PORT=5432\nSECRET_KEY=mysecret123\n")

env_vars = {}
if os.path.exists(".env"):
    with open(".env", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

print(".env faylidan o'qilgan o'zgaruvchilar:", env_vars)
