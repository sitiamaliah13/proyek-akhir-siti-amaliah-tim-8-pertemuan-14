
# Modul untuk membaca data nilai dari file

def baca_data(nama_file):
    """Membaca data nilai dari file teks."""
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if baris:
                    data.append(float(baris))

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    except ValueError:
        print("File berisi data yang bukan angka.")

    return data
