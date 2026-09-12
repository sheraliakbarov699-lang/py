import json
import logging

config_data = '{"app_name": "MyApp", "debug": true}'
config = json.loads(config_data)

log_level = logging.DEBUG if config.get("debug") else logging.INFO
logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

logging.info("Ilova ishga tushdi.")
if config.get("debug"):
    logging.debug("Qo'shimcha DEBUG ma'lumoti: Konfiguratsiya to'liq yuklandi.")
