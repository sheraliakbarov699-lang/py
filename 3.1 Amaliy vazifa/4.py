import csv

xodimlar = [
    ["ID", "Ism", "Lavozim", "Oylik"],
    [1, "Ali", "DevOps Engineer", 1500],
    [2, "Vali", "Backend Developer", 1800],
    [3, "Soli", "System Administrator", 1400]
]

with open("xodimlar.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(xodimlar)

with open("xodimlar.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("\nXodimlar Jadvali:")
    print("-" * 40)
    for row in reader:
        print(f"{row[0]:<5} | {row[1]:<10} | {row[2]:<20} | {row[3]:<6}")
    print("-" * 40)
