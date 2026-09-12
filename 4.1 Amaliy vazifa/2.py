import sys

if len(sys.argv) < 2:
    print("Xatolik: Fayl nomini argument sifatida kiriting!")
    print("Ishlatish: python 2.py <fayl_nomi>")
else:
    file_name = sys.argv[1]
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            print(f"--- {file_name} fayli mazmuni ---")
            print(f.read())
    except FileNotFoundError:
        print(f"Xatolik: '{file_name}' fayli topilmadi!")
