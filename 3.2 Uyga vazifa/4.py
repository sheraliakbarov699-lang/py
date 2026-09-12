import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app_rotating.log", maxBytes=1024*1024, backupCount=3)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger = logging.getLogger("RotatingLogger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info("RotatingFileHandler muvaffaqiyatli sozlandi.")
print("Rotating log sozlamasi yaratildi.")
