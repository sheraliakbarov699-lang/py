import os

def find_tmp_files(directory="."):
    tmp_files = [f for f in os.listdir(directory) if f.endswith(".tmp")]
    print(f"'{directory}' papkasidagi .tmp fayllar ro'yxati:")
    if tmp_files:
        for f in tmp_files:
            print(f"- {f}")
    else:
        print(".tmp fayllar topilmadi.")

find_tmp_files()
