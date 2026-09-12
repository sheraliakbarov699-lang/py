import yaml

servers = {
    "servers": [
        {"name": "web-01", "ip": "192.168.1.10", "role": "frontend"},
        {"name": "db-01", "ip": "192.168.1.20", "role": "database"}
    ]
}

with open("servers.yaml", "w", encoding="utf-8") as f:
    yaml.dump(servers, f, default_flow_style=False)

with open("servers.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

print("YAML fayldan o'qilgan serverlar:", data)
