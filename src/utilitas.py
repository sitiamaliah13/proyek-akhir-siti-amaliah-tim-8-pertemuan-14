
# Modul untuk fungsi bantuan program

def tampilkan_judul():
    """Menampilkan judul aplikasi."""
    print("=" * 40)
    print("APLIKASI ANALISIS DATA NILAI")
    print("=" * 40)


def tampilkan_menu():
    """Menampilkan menu utama."""
    print("\nMenu:")
    print("1. Tampilkan semua nilai")
    print("2. Hitung rata-rata")
    print("3. Cari nilai tertinggi")
    print("4. Cari nilai terendah")
    print("5. Keluar")


def minta_pilihan():
    """Meminta pilihan menu dari pengguna."""
    return input("Pilih menu (1-5): ").strip()
