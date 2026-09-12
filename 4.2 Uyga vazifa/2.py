import shutil

total, used, free = shutil.disk_usage("/")
free_gb = free / (1024 ** 3)
threshold_gb = 10.0  # Chegara: 10 GB

print(f"Bo'sh joy: {free_gb:.2f} GB")
if free_gb < threshold_gb:
    print(f"OGOHLANTIRISH: Diskda bo'sh joy {threshold_gb} GB dan kam qoldi!")
else:
    print("Disk xotirasi yetarli.")
