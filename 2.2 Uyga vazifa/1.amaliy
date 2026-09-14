def check_down_servers(monitoring):
    for server, status in monitoring.items():
        if status == "down":
            print(f"Istdan chiqqan server: {server}")

servers = {
    "web-01": "up",
    "db-01": "down",
    "cache-01": "up",
    "api-01": "down"
}

check_down_servers(servers)
