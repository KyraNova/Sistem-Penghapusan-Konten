import os
from utils.file_manager import read_list, remove_content

def main(file_path="data/list_konten.txt"):
    # Periksa apakah file ada
    if not os.path.exists(file_path):
        print(f"File {file_path} tidak ditemukan! Membuat file baru...")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("")
        print(f"File {file_path} berhasil dibuat. Silakan tambahkan konten ke file ini.")
        return

    # Jika file ada, lanjutkan
    print("Daftar Konten:")
    konten = read_list(file_path)
    if not konten:
        print("File kosong, tidak ada konten yang dapat ditampilkan.")
        return

    for idx, item in enumerate(konten, 1):
        print(f"{idx}. {item.strip()}")

    try:
        pilihan = int(input("\nMasukkan nomor konten yang ingin dihapus: "))
        if 1 <= pilihan <= len(konten):
            removed_item = konten.pop(pilihan - 1)
            remove_content(file_path, konten)
            print(f"\nKonten '{removed_item.strip()}' berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

if __name__ == "__main__":
    main()
