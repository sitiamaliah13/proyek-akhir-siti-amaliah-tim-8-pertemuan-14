
# Proyek Pertemuan 14: Aplikasi Analisis Data Nilai
# Nama: Siti Amaliah
# NIM: 2225250223
# Kelas: 3E

from data_io import baca_data
from analisis import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
)
from utilitas import tampilkan_judul, tampilkan_menu, minta_pilihan


def main():
    tampilkan_judul()

    data = baca_data("data/nilai_contoh.txt")

    if not data:
        print("Belum ada data nilai yang dapat diproses.")
        return

    while True:
        tampilkan_menu()
        pilihan = minta_pilihan()

        if pilihan == "1":
            print("Data nilai:", data)

        elif pilihan == "2":
            rata_rata = hitung_rata_rata(data)
            print(f"Rata-rata nilai: {rata_rata:.2f}")

        elif pilihan == "3":
            tertinggi = cari_nilai_tertinggi(data)
            print(f"Nilai tertinggi: {tertinggi}")

        elif pilihan == "4":
            terendah = cari_nilai_terendah(data)
            print(f"Nilai terendah: {terendah}")

        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    main()
