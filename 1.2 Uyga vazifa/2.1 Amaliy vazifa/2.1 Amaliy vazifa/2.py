serverlar = {
    "web-server": "192.168.1.10",
    "db-server": "192.168.1.20",
    "cache-server": "192.168.1.30"
}

for name, ip in serverlar.items():
    print(f"Server: {name} | IP: {ip}")
