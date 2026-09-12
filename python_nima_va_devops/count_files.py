import argparse
from pathlib import Path


def count_files(folder: str) -> int:
    path = Path(folder)
    if not path.is_dir():
        raise NotADirectoryError(f"'{folder}' papka topilmadi")
    return sum(1 for item in path.iterdir() if item.is_file())


def main():
    parser = argparse.ArgumentParser(description="Berilgan papkadagi fayllar sonini sanaydi")
    parser.add_argument("folder", nargs="?", default=".", help="Papka yoli (default: joriy papka)")
    args = parser.parse_args()

    try:
        total = count_files(args.folder)
        print(f"'{args.folder}' papkasida {total} ta fayl bor.")
    except NotADirectoryError as e:
        print(f"Xatolik: {e}")


if __name__ == "__main__":
    main()
