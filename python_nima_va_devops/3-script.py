import argparse


def start(args):
    print(f"Xizmat ishga tushirildi. Port: {args.port}")


def stop(args):
    print(f"Xizmat to'xtatildi. Force: {args.force}")


def main():
    parser = argparse.ArgumentParser(description="Oddiy xizmat boshqaruvchisi")
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="Xizmatni ishga tushirish")
    start_parser.add_argument("--port", type=int, default=8080, help="Port raqami")
    start_parser.set_defaults(func=start)

    stop_parser = subparsers.add_parser("stop", help="Xizmatni to'xtatish")
    stop_parser.add_argument("--force", action="store_true", help="Majburiy to'xtatish")
    stop_parser.set_defaults(func=stop)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
