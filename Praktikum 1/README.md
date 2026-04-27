# 🧠 Lexical Analyzer (Web-Based)

## 📌 Deskripsi

Program ini merupakan implementasi sederhana dari **Lexical Analyzer (Lexer)** yang bertujuan untuk membaca input berupa teks (kode/program), kemudian memecahnya menjadi token-token dan mengelompokkannya berdasarkan jenisnya.

Aplikasi ini dibuat berbasis **web (HTML + JavaScript)** sehingga dapat dijalankan langsung di browser tanpa memerlukan backend atau instalasi tambahan.

---

## 🎯 Tujuan

* Mengidentifikasi token dalam suatu input teks
* Mengelompokkan token ke dalam kategori tertentu
* Memberikan visualisasi hasil analisis secara interaktif

---

## ⚙️ Fitur Utama

Program ini mampu mendeteksi dan mengelompokkan:

1. **Reserved Words**
   Kata kunci dalam bahasa pemrograman seperti:

   ```
   if, else, while, for, return, int, float, dll
   ```

2. **Variabel (Identifier)**
   Nama variabel yang diawali huruf atau underscore
   Contoh:

   ```
   x, nilai, data_1
   ```

3. **Operator**
   Simbol operasi matematika atau logika
   Contoh:

   ```
   +, -, *, /, =, <, >
   ```

4. **Simbol / Tanda Baca**
   Karakter khusus dalam sintaks
   Contoh:

   ```
   ; ( ) { } [ ] ,
   ```

5. **Angka (Number)**
   Bilangan bulat maupun desimal
   Contoh:

   ```
   10, 3.14
   ```

6. **Unknown**
   Karakter yang tidak termasuk kategori di atas
   Contoh:

   ```
   ?, @, #
   ```

---

## 🖥️ Cara Menjalankan

1. Simpan file sebagai:

   ```
   index.html
   ```

2. Buka file dengan:

   * Double click
     atau
   * Gunakan Live Server di VSCode

3. Masukkan teks/kode pada textarea

4. Klik tombol **Analyze**

5. Hasil akan muncul di bawah tombol

---

## 🧪 Contoh Input

```
int x = 5;
x = x + y;
kamu keren sekali?
```

## 📤 Contoh Output

```
Reserved Words : int
Variabel       : x y kamu keren sekali
Operator       : = +
Simbol         : ;
Angka          : 5
Unknown        : ?
```

---

## 🧩 Cara Kerja Program

### 1. Tokenisasi

Program menggunakan **Regular Expression (Regex)** untuk memecah input menjadi token-token:

```javascript
const tokens = code.match(/\d+(\.\d+)?|[a-zA-Z_][a-zA-Z0-9_]*|[\+\-\*\/=<>!]+|[()\{\}\[\];,]|./g);
```

### 2. Klasifikasi Token

Setiap token diperiksa dan dimasukkan ke kategori sesuai aturan:

* Angka → NUMBER
* Kata kunci → RESERVED WORD
* Huruf → VARIABLE
* Operator → OPERATOR
* Simbol → SYMBOL
* Selain itu → UNKNOWN

---

## 🧠 Konsep yang Digunakan

* Lexical Analysis (Compiler Design)
* Regular Expression (Regex)
* Array & String Processing
* DOM Manipulation (JavaScript)

---

## 🎨 Tampilan

* Input menggunakan textarea
* Output ditampilkan dalam bentuk card
* Hanya kategori yang memiliki isi yang ditampilkan

---

## ⚠️ Keterbatasan

* Tidak mendukung parsing lanjutan (syntax analysis)
* Tidak membedakan tipe variabel
* Tidak mendeteksi scope
* Belum mendukung string literal atau komentar

---

## 🚀 Pengembangan Lanjutan

Beberapa pengembangan yang bisa dilakukan:

* Syntax highlighting (warna token)
* Real-time analysis (tanpa tombol)
* Tabel hasil token
* Support multi-line lebih kompleks
* Integrasi dengan parser

---

## 👨‍💻 Author

Dibuat untuk keperluan tugas mata kuliah terkait **Compiler / Automata / Bahasa Formal**

---

## 📌 Kesimpulan

Program ini berhasil mengimplementasikan konsep dasar **Lexical Analyzer** dengan pendekatan sederhana berbasis web, sehingga mudah digunakan, dipahami, dan dikembangkan lebih lanjut.
