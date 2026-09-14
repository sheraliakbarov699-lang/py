def validate_port(port_input):
    try:
        port = int(port_input)
        if 1 <= port <= 65535:
            return f"To'g me'ri port: {port}"
        else:
            return "Xatolik: Port raqami 1 va 65535 oralig'ida bo'lishi kerak!"
    except ValueError:
        return "Xatolik: Port raqami faqat butun sonlardan iborat bo'lishi kerak!"

print(validate_port("8080"))
print(validate_port("70000"))
print(validate_port("abc"))
