import argparse


def main():
    parser = argparse.ArgumentParser(description="Foydalanuvchiga salomlashuv xabari chiqaradi")
    parser.add_argument("--name", required=True, help="Salomlashiladigan shaxsning ismi")
    args = parser.parse_args()

    print(f"Salom, {args.name}! Xush kelibsiz.")


if __name__ == "__main__":
    main()
