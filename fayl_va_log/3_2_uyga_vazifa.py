import json
import yaml
import csv
import logging
from logging.handlers import RotatingFileHandler
import glob

# 1-topshiriq: JSON-dagi debug statusiga qarab log darajasini belgilash
config = {"env": "prod", "debug": True}
log_level = logging.DEBUG if config.get("debug") else logging.INFO

logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")
if config.get("debug"):
    logging.debug("DEBUG rejimi yoqilgan: Barcha ma'lumotlar ko'rsatilmoqda.")

# 2-topshiriq: YAML <-> JSON konverter
def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as yf:
        data = yaml.safe_load(yf)
    with open(json_file, 'w') as jf:
        json.dump(data, jf, indent=4)

def json_to_yaml(json_file, yaml_file):
    with open(json_file, 'r') as jf:
        data = json.load(jf)
    with open(yaml_file, 'w') as yf:
        yaml.dump(data, yf)

# 3-topshiriq: Katta CSV faylni qatorma-qator o'qib 'error' statuslilarini ajratish
sample_logs = [
    ["timestamp", "status", "message"],
    ["2026-09-11 10:00", "info", "System boot"],
    ["2026-09-11 10:05", "error", "Database connection failed"],
    ["2026-09-11 10:10", "error", "Disk full warning"]
]
with open("system_logs.csv", "w", newline="") as f:
    csv.writer(f).writerows(sample_logs)

with open("system_logs.csv", "r") as infile, open("errors_only.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        if len(row) > 1 and row[1] == "error":
            writer.writerow(row)

# 4-topshiriq: RotatingFileHandler sozlash (1MB hajmgacha)
logger = logging.getLogger("RotatingLogger")
handler = RotatingFileHandler("app_rotating.log", maxBytes=1*1024*1024, backupCount=3)
logger.addHandler(handler)
logger.warning("Rotating handler orqali test log xabari.")

# 5-topshiriq: Barcha .log fayllarni tekshirib, "ERROR" so'zi borlarini hisobotga yozish
with open("error_report.txt", "w") as report:
    for log_file in glob.glob("*.log"):
        with open(log_file, "r") as f:
            for line in f:
                if "ERROR" in line:
                    report.write(f"[{log_file}] {line}")

print("3.2 Uyga vazifa barcha topshiriqlari bajarildi.")
