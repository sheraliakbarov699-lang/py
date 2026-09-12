import os

report_file = "error_report.txt"

with open(report_file, "w", encoding="utf-8") as report:
    for file in os.listdir("."):
        if file.endswith(".log"):
            with open(file, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    if "ERROR" in line:
                        report.write(f"Fayl: {file} | Qator {line_num}: {line.strip()}\n")

print(f"Barcha .log fayllardagi ERROR yozuvlari {report_file} fayliga saqlandi.")
