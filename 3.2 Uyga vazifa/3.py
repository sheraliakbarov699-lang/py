import csv

# Test uchun namunaviy CSV fayl yaratamiz
with open("large_log.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "message", "status"])
    writer.writerow([1, "User login", "info"])
    writer.writerow([2, "Connection timed out", "error"])
    writer.writerow([3, "Page loaded", "info"])
    writer.writerow([4, "Database error", "error"])

# Qatorma-qator o'qib filterlash
with open("large_log.csv", "r", encoding="utf-8") as infile, \
     open("errors_only.csv", "w", newline="", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    writer.writerow(header)
    
    for row in reader:
        if len(row) >= 3 and row[2] == "error":
            writer.writerow(row)

print("Status == 'error' bo'lgan qatorlar errors_only.csv fayliga ajratildi.")
