class InvalidServerNameError(Exception):
    pass

def check_server_name(name):
    if not name.startswith("srv-"):
        raise InvalidServerNameError(f"Noto'g'ri server nomi: {name}. Nomi 'srv-' bilan boshlanishi kerak!")
    print(f"Server nomi to'g'ri: {name}")

try:
    check_server_name("web-server")
except InvalidServerNameError as e:
    print("Xatolik ushlandi:", e)
