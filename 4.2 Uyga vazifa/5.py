import shutil
import os
from datetime import datetime

source_dir = "my_data"
os.makedirs(source_dir, exist_ok=True)

# Test fayl yaratamiz
with open(f"{source_dir}/sample.txt", "w") as f:
    f.write("Backup test data")

date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_dir = f"backup_{date_str}"

shutil.copytree(source_dir, backup_dir)
print(f"Papkani zaxira nusxasi yaratildi: {backup_dir}")
