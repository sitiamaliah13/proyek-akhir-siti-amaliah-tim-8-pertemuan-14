# Aplikasi Analisis Data Nilai

## 1. Identitas Mahasiswa

- **Nama:** Siti Amaliah
- **NIM:** 2225250223
- **Kelas:** 3E
- **Program Studi:** S1 Pendidikan Matematika
- **Fakultas:** FKIP
- **Universitas:** Universitas Sultan Ageng Tirtayasa (Untirta)

## 2. Deskripsi Proyek

Aplikasi Analisis Data Nilai merupakan program sederhana berbasis Python yang digunakan untuk membaca dan menganalisis data nilai dari file teks. Program ini membantu pengguna melihat kumpulan nilai, menghitung rata-rata, serta mengetahui nilai tertinggi dan nilai terendah.

Proyek ini dibuat sebagai bagian dari tugas Perancangan Proyek pada Pertemuan 14.

## 3. Tujuan Proyek

1. Menerapkan dasar pemrograman Python dalam sebuah proyek.
2. Membaca data nilai dari file teks.
3. Mengolah data nilai menggunakan fungsi Python.
4. Menerapkan pemisahan program ke dalam beberapa modul.
5. Melakukan pengujian terhadap fitur-fitur program.

## 4. Fitur Program

- Membaca data nilai dari file `data/nilai_contoh.txt`.
- Menampilkan seluruh data nilai.
- Menghitung rata-rata nilai.
- Menentukan nilai tertinggi.
- Menentukan nilai terendah.
- Menangani pilihan menu yang tidak valid.
- Menampilkan pesan ketika file data tidak ditemukan.

## 5. Struktur Folder Proyek

```text
proyek-akhir-nama-tim/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

Keterangan:
- `README.md`: berisi informasi dan petunjuk penggunaan proyek.
- `proposal.md`: berisi rancangan proposal proyek.
- `.gitignore`: menentukan file yang tidak perlu disertakan dalam Git.
- `data/nilai_contoh.txt`: menyimpan data nilai yang akan dianalisis.
- `src/main.py`: menjalankan program utama.
- `src/data_io.py`: membaca data nilai dari file.
- `src/analisis.py`: melakukan perhitungan dan analisis nilai.
- `src/utilitas.py`: menyediakan fungsi tampilan judul dan menu.
- `tests/test_case.md`: berisi daftar skenario pengujian program.
- `output/.gitkeep`: menjaga agar folder output tetap tercatat di repository.

## 6. Teknologi yang Digunakan

- Bahasa pemrograman Python 3.
- Visual Studio Code sebagai editor kode.
- Git untuk pengelolaan versi.
- GitHub sebagai tempat penyimpanan repository proyek.

## 7. Cara Menjalankan Program

**Persyaratan:** Python 3 sudah terpasang di komputer.

1. Buka folder proyek menggunakan Visual Studio Code.
2. Pastikan file `data/nilai_contoh.txt` sudah berisi data nilai.
3. Buka terminal di folder utama proyek.
4. Jalankan perintah berikut:

```bash
python src/main.py
```

5. Pilih menu sesuai fitur yang ingin digunakan:
   - `1` untuk menampilkan semua nilai.
   - `2` untuk menghitung rata-rata.
   - `3` untuk mencari nilai tertinggi.
   - `4` untuk mencari nilai terendah.
   - `5` untuk keluar dari program.

## 8. Contoh Data

File `data/nilai_contoh.txt` berisi:

```text
80
75
90
85
70
95
88
```

## 9. Contoh Hasil Program

```text
========================================
APLIKASI ANALISIS DATA NILAI
========================================

Menu:
1. Tampilkan semua nilai
2. Hitung rata-rata
3. Cari nilai tertinggi
4. Cari nilai terendah
5. Keluar
```

Berdasarkan data contoh, hasil analisisnya adalah:

- **Jumlah data:** 7 nilai.
- **Rata-rata:** 83.29.
- **Nilai tertinggi:** 95.
- **Nilai terendah:** 70.

## 10. Pengujian Program

Pengujian dilakukan dengan mencoba fitur-fitur program, meliputi:

1. Menampilkan seluruh data nilai.
2. Menghitung rata-rata nilai.
3. Menentukan nilai tertinggi.
4. Menentukan nilai terendah.
5. Memasukkan pilihan menu yang tidak valid.
6. Keluar dari program.

Daftar skenario pengujian dapat dilihat pada file `tests/test_case.md`.

## 11. Repository GitHub

Repository proyek dapat diakses melalui tautan berikut:

https://github.com/sitiamaliah13/proyek-akhir-siti-amaliah-tim-8-pertemuan-14

## 12. Pengembangan Selanjutnya

Pengembangan berikutnya dapat mencakup validasi nilai dalam rentang 0–100, pengelompokan nilai berdasarkan KKM, serta penyimpanan hasil analisis ke dalam file laporan.

---

**Catatan:** Proyek ini merupakan rancangan dan implementasi awal aplikasi analisis data nilai untuk tugas Perancangan Proyek Pertemuan 14.
