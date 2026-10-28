# Test Case — Kalkulator Geometri Bangun Datar

## Tujuan Pengujian

Pengujian dilakukan untuk memeriksa apakah program dapat menghitung luas dan keliling bangun datar serta menangani masukan pengguna dengan benar.

## Daftar Test Case

| No. | Skenario Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Menghitung luas dan keliling persegi | Sisi = 4 | Luas = 16 dan keliling = 16 |
| 2 | Menghitung luas dan keliling persegi panjang | Panjang = 5, lebar = 3 | Luas = 15 dan keliling = 16 |
| 3 | Menghitung luas dan keliling lingkaran | Jari-jari = 7 | Luas sekitar 153,94 dan keliling sekitar 43,98 |
| 4 | Memasukkan ukuran nol | Sisi = 0 | Luas = 0 dan keliling = 0 |
| 5 | Memasukkan ukuran negatif | Sisi = -2 | Program menolak masukan atau menampilkan pesan kesalahan |
| 6 | Memasukkan teks sebagai ukuran | Sisi = abc | Program menampilkan pesan kesalahan dan tidak berhenti secara tiba-tiba |
| 7 | Memilih menu yang tidak tersedia | Pilihan = 9 | Program menampilkan pesan pilihan tidak valid |

## Kriteria Keberhasilan

Pengujian dinyatakan berhasil apabila:
1. Hasil perhitungan sesuai dengan rumus bangun datar.
2. Program menangani ukuran nol sesuai rancangan.
3. Masukan negatif ditangani sesuai aturan program.
4. Masukan bukan angka tidak menyebabkan program berhenti secara tiba-tiba.
5. Pilihan menu yang tidak valid menghasilkan pesan yang sesuai.

**Catatan:** Test case ini merupakan rancangan pengujian. Hasil aktual baru dapat dicatat setelah program selesai diimplementasikan dan diuji.