# 1-topshiriq: Monitoring dict va statusi "down" bo'lgan serverlarni chop etish
monitoring = {
    "web-01": "up",
    "db-01": "down",
    "api-01": "up",
    "redis-01": "down"
}
def check_down_servers(mon_dict):
    print("Statusi 'down' bo'lgan serverlar:")
    for server, status in mon_dict.items():
        if status == "down":
            print(f"- {server}")

# 2-topshiriq: List comprehension bilan 1-50 oralig'ida 3 ga bo'linadigan sonlar
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]

# 3-topshiriq: Nested function va Closure misoli
def outer_function(msg):
    def inner_function():
        print(f"Closure orqali yetkazilgan xabar: {msg}")
    return inner_function

# 4-topshiriq: Custom exception InvalidServerNameError
class InvalidServerNameError(Exception):
    pass

def validate_server_name(name):
    if not name.startswith("srv-"):
        raise InvalidServerNameError(f"Xato server nomi: '{name}'. Server nomi 'srv-' bilan boshlanishi kerak!")
    print(f"Server nomi to'g'ri: {name}")

# 5-topshiriq: Port raqamini tekshiruvchi validatsiya skripti
def validate_port(port_input):
    try:
        port = int(port_input)
        if 1 <= port <= 65535:
            print(f"Port to'g'ri kiritildi: {port}")
        else:
            print("Xatolik: Port raqami 1 va 65535 oralig'ida bo'lishi kerak!")
    except ValueError:
        print("Xatolik: Port raqami faqat butun sonlardan iborat bo'lishi lozim!")

if __name__ == "__main__":
    print("--- 2.2 UYGA VAZIFA ---")
    check_down_servers(monitoring)
    
    print("\n3 ga bo'linadigan sonlar (1-50):", divisible_by_3)
    
    print("\nClosure misoli:")
    my_closure = outer_function("Hello DevOps!")
    my_closure()
    
    print("\nCustom Exception misoli:")
    try:
        validate_server_name("web-server-1")
    except InvalidServerNameError as e:
        print("Ushlangan Exception:", e)
        
    print("\nPort validatsiyasi testi:")
    validate_port("8080")
    validate_port("invalid_port")
