# Tugas Praktikum 2 - Otomata

## Identitas Kelompok
- **Nama**: Jonathan Purba; Jhonatan Simorangkir
- **NRP**: 5025221132; 5025221316

## Deskripsi Tugas
Program ini dirancang untuk menentukan apakah suatu *string* merupakan anggota dari himpunan bahasa:
**$L = \{ x \in (0 + 1)^+ \mid \text{karakter terakhir pada string } x \text{ adalah 1 dan } x \text{ tidak memiliki substring 00} \}$**.

## Logika Algoritma (FSM)
Implementasi kode ini didasarkan pada *Finite State Diagram* dengan 4 state utama:

| State | Deskripsi |
|-------|-----------|
| **S** | *Start State*: Titik awal mesin sebelum membaca input. |
| **A** | State transisi setelah membaca karakter `0`. |
| **B** | *Final State*: String diterima jika berakhir di sini (menandakan akhiran `1`). |
| **C** | *Trap State*: State mati jika ditemukan substring `00`. Sekali masuk ke sini, string otomatis ditolak. |

### Aturan Transisi:
- **Dari S**: Input `0` → A; Input `1` → B.
- **Dari A**: Input `0` → C (*Trap*); Input `1` → B.
- **Dari B**: Input `0` → A; Input `1` → B.
- **Dari C**: Input `0` atau `1` → Tetap di C.

## Fitur Program
Program dibuat menggunakan **HTML, CSS, dan JavaScript** untuk menampilkan UI/UX yang lebih menarik dan fresh:

1. **Validasi Input Real-time**: Program secara otomatis mendeteksi dan memberi peringatan jika pengguna memasukkan karakter selain `0` dan `1`.
2. **Visualisasi Path Trace**: Menampilkan urutan perpindahan *state* secara detail langkah demi langkah (misal: `S → A → B`) sehingga memudahkan proses verifikasi algoritma.

---
*Dibuat untuk memenuhi tugas mata kuliah Otomata - Teknik Informatika ITS.*