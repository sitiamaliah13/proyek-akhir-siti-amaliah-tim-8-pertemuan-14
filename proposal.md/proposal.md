# PROPOSAL PROYEK PERTEMUAN 14
## Aplikasi Analisis Data Nilai

### Identitas Mahasiswa
- **Nama:** Siti Amaliah
- **NIM:** 2225250223
- **Kelas:** 3E
- **Program Studi:** S1 Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman

## 1. Judul Proyek
**Aplikasi Analisis Data Nilai**

## 2. Latar Belakang
Pengolahan data nilai secara manual membutuhkan waktu dan dapat menimbulkan kesalahan dalam perhitungan. Oleh karena itu, diperlukan program sederhana yang dapat membaca data nilai dari file teks, menampilkan seluruh data, menghitung rata-rata, serta menentukan nilai tertinggi dan terendah secara otomatis.

Proyek ini dirancang menggunakan Python dengan pembagian program ke dalam beberapa modul agar kode lebih terstruktur dan mudah diuji.

## 3. Pengguna dan Tujuan
**Pengguna:** Mahasiswa, guru, atau pengguna yang membutuhkan pengolahan data nilai sederhana.

**Tujuan:**
1. Membaca data nilai dari file teks.
2. Menampilkan seluruh data nilai.
3. Menghitung rata-rata nilai.
4. Menentukan nilai tertinggi dan terendah.
5. Menangani pilihan menu yang tidak valid dan kondisi file tidak ditemukan.

## 4. Ruang Lingkup
**Fitur yang direncanakan:**
- Membaca data angka dari `data/nilai_contoh.txt`.
- Menampilkan daftar nilai.
- Menghitung rata-rata nilai.
- Mencari nilai tertinggi dan terendah.
- Menampilkan menu interaktif melalui terminal.
- Menangani pilihan menu yang tidak valid dan file yang tidak ditemukan.

**Batasan proyek:**
- Program berjalan melalui terminal menggunakan Python.
- Data masukan disimpan dalam file teks.
- Data contoh berupa angka nilai, bukan data mahasiswa lengkap.
- Penyimpanan laporan hasil ke file belum termasuk fitur versi awal.

## 5. Kebutuhan

### A. Kebutuhan Fungsional
1. Program dapat membaca data nilai dari file teks.
2. Program dapat menampilkan data nilai.
3. Program dapat menghitung rata-rata nilai.
4. Program dapat menentukan nilai tertinggi dan terendah.
5. Program dapat menerima pilihan menu dari pengguna.
6. Program dapat menampilkan pesan jika pilihan menu tidak valid.
7. Program dapat menangani kondisi file tidak ditemukan.

### B. Kebutuhan Nonfungsional
1. Program ditulis menggunakan Python 3.
2. Program memiliki modul dengan tanggung jawab yang jelas.
3. Tampilan menu dan hasil mudah dibaca.
4. Program dapat dijalankan melalui terminal di VS Code.
5. Kesalahan masukan atau file ditangani dengan pesan yang sesuai.

## 6. Input, Process, Output (IPO)

| Input | Proses | Output |
|---|---|---|
| File `data/nilai_contoh.txt` | Membaca dan menyimpan nilai ke dalam list | Daftar nilai |
| Pilihan menu 1 | Menampilkan seluruh data | Daftar nilai ditampilkan |
| Pilihan menu 2 | Menjumlahkan nilai lalu membaginya dengan banyak data | Rata-rata nilai |
| Pilihan menu 3 | Mencari nilai terbesar | Nilai tertinggi |
| Pilihan menu 4 | Mencari nilai terkecil | Nilai terendah |
| Pilihan menu 5 | Mengakhiri perulangan program | Pesan program selesai |
| Pilihan menu selain 1–5 | Memeriksa validitas pilihan | Pesan pilihan tidak valid |

## 7. Algoritma

### Pseudocode
1. Mulai.
2. Tampilkan judul aplikasi.
3. Baca data nilai dari file teks.
4. Jika file tidak ditemukan atau data tidak dapat dibaca, tampilkan pesan yang sesuai dan hentikan program jika tidak ada data yang dapat diproses.
5. Tampilkan menu pilihan.
6. Minta pengguna memasukkan pilihan menu.
7. Jika pilihan adalah 1, tampilkan semua nilai.
8. Jika pilihan adalah 2, hitung dan tampilkan rata-rata nilai.
9. Jika pilihan adalah 3, cari dan tampilkan nilai tertinggi.
10. Jika pilihan adalah 4, cari dan tampilkan nilai terendah.
11. Jika pilihan adalah 5, tampilkan pesan selesai dan akhiri program.
12. Jika pilihan tidak sesuai, tampilkan pesan pilihan tidak valid.
13. Kembali ke menu selama pengguna belum memilih keluar.
14. Selesai.

## 8. Struktur Program

Struktur folder proyek direncanakan sebagai berikut:

```text
proyek-akhir-siti-amaliah-tim-8-pertemuan-14/
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

**Tanggung jawab modul:**
- `main.py`: mengatur alur utama dan menghubungkan modul.
- `data_io.py`: membaca data nilai dari file teks.
- `analisis.py`: menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- `utilitas.py`: menampilkan judul, menu, dan menerima pilihan pengguna.
- `nilai_contoh.txt`: menyimpan data nilai contoh.
- `test_case.md`: mencatat skenario pengujian.
- `README.md`: menjelaskan proyek dan cara menjalankannya.

## 9. Struktur Data
1. **List:** menyimpan kumpulan nilai yang dibaca dari file.
2. **String:** menyimpan setiap baris teks, pilihan menu, dan pesan program.
3. **File teks:** menyimpan data nilai yang akan dibaca oleh program.
4. **Bilangan numerik:** digunakan untuk menyimpan dan menghitung nilai serta hasil rata-rata.

## 10. Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Pilih menu 1 | Semua nilai ditampilkan |
| TC02 | Normal | Pilih menu 2 | Rata-rata tujuh nilai adalah 83.29 |
| TC03 | Normal | Pilih menu 3 | Nilai tertinggi adalah 95 |
| TC04 | Normal | Pilih menu 4 | Nilai terendah adalah 70 |
| TC05 | Invalid | Pilih menu 9 | Pesan pilihan tidak valid ditampilkan |
| TC06 | Normal | Pilih menu 5 | Program berhenti dengan pesan selesai |
| TC07 | Invalid | File data tidak ditemukan | Program menampilkan pesan file tidak ditemukan |

## 11. Pembagian Tugas
Proyek dikerjakan secara individu oleh Siti Amaliah.

| Peran | Penanggung Jawab | Tanggung Jawab |
|---|---|---|
| Koordinator proyek | Siti Amaliah | Menentukan ruang lingkup dan mengintegrasikan program |
| Programmer Data I/O | Siti Amaliah | Membuat fungsi pembacaan file |
| Programmer logika | Siti Amaliah | Membuat fungsi analisis nilai |
| Tester/QA | Siti Amaliah | Menyusun dan menjalankan pengujian |
| Dokumentasi | Siti Amaliah | Menyusun proposal dan README serta mengelola repository |

## 12. Jadwal

| Tahap | Target |
|---|---|
| Pertemuan 14 | Menyelesaikan proposal, struktur folder, algoritma, dan test case |
| Antara Pertemuan 14–15 | Menyelesaikan implementasi awal fitur wajib |
| Pertemuan 15 | Integrasi, pengujian, debugging, dan dokumentasi |
| Pertemuan 16 | Presentasi, demonstrasi, dan evaluasi proyek |

## 13. Repository
URL GitHub: https://github.com/sitiamaliah13/proyek-akhir-siti-amaliah-tim-8-pertemuan-14

## Penutup
Proposal ini menjadi acuan pengembangan Aplikasi Analisis Data Nilai pada tahap implementasi dan pengujian berikutnya. Program akan dikembangkan secara bertahap dengan memperhatikan kebutuhan, algoritma, struktur modul, dan hasil pengujian.

**Catatan bantuan:** Penyusunan rancangan dibantu menggunakan ChatGPT. Pemilik proyek bertanggung jawab memahami dan memeriksa isi proposal serta program.