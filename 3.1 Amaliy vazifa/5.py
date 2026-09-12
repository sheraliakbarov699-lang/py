import logging

logging.basicConfig(
    filename="system_events.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Skript ishi boshlandi (Start)")

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Nolga bo'lish xatoligi yuz berdi (Xatolik)")

logging.info("Skript ishi yakunlandi (Tugash)")
print("Voqealar system_events.log fayliga yozildi.")
