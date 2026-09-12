import subprocess

service_name = "nginx"

def check_and_restart():
    # Service holatini tekshirish
    check = subprocess.run(["pgrep", service_name], capture_output=True, text=True)
    if check.returncode != 0:
        print(f"Xizmat ({service_name}) ishlamayapti. Qayta ishga tushirilmoqda...")
        subprocess.run(["sudo", "systemctl", "start", service_name])
    else:
        print(f"Xizmat ({service_name}) faol ishlamoqda.")

print(f"{service_name} xizmati monitoringi bajarildi.")
