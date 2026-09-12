import datetime

log_msg = f"{datetime.datetime.now()}: Monitoring skripti har 5 daqiqada muvaffaqiyatli ishga tushdi.\n"

with open("cron_monitor.log", "a", encoding="utf-8") as f:
    f.write(log_msg)

print("Cron log yozildi.")
"""
Crontab sozlamasi (terminalda `crontab -e` buyrug'i orqali qo'shiladi):
*/5 * * * * /usr/bin/python3 /path/to/4.2\ Uyga\ vazifa/4.py
"""
