# K-3 Analisis dan Penanganan Deadlock - Kelompok 4 (Kelas D)

Mata Kuliah Sistem Operasi (USA-WP2260110), Universitas Sebelas April.
Tema: Cloud dan Layanan Digital UMKM (checkout toko online).

## Anggota
| Nama | NIM | Peran |
|---|---|---|
| Risca Fazriah Syabania | 250660121080 | Leader |
| Adrian Hidayat | 250660121007 | Anggota 1 |
| Fitria Salsabila Al-Qusyaeri | 250660121060 | Anggota 2 |

## Isi
- `banker.py` : simulasi algoritma Banker (Need, safe state, safe sequence, uji permintaan)
- `log_banker.txt` : keluaran `python3 banker.py`

## Sumber daya
- R1 = lock tabel stok
- R2 = lock transaksi pembayaran
- R3 = slot kurir

## Cara menjalankan
```
python3 banker.py
```
Hanya memakai Python 3 tanpa pustaka tambahan.

## Matriks
Matriks Allocation, Max, dan Available diambil dari data kelas yang dibagikan dosen
(variabel `alloc`, `mx`, `avail` di bagian atas `banker.py`).
