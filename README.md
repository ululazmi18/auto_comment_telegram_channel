Tentu! Berikut adalah isi README.md yang diformat agar mudah disalin sekaligus:

```markdown
# README.md

## Keterangan
Skrip ini memungkinkan pengguna untuk mengirim pesan otomatis ke saluran Telegram. Pesan yang dikirim dapat menyertakan media (gambar atau video) yang disimpan dalam folder `media`. Skrip ini juga secara otomatis bergabung dengan saluran yang diperlukan jika belum terdaftar.

## Fungsi
Skrip ini mengirimkan pesan dan media secara otomatis ke saluran Telegram yang ditentukan. Pengguna dapat mengonfigurasi pengaturan seperti API ID, Hash Telegram, nomor telepon, dan delay pengiriman pesan.

## Fitur
- Mengirim pesan teks dari file .txt secara acak.
- Menyertakan media (gambar atau video) dalam pesan.
- Bergabung secara otomatis dengan saluran jika belum terdaftar.
- Konfigurasi delay antara pengiriman pesan.
- Membuat folder dan file konfigurasi secara otomatis.

## Langkah-langkah Instalasi

### Windows
1. **Instal Python**: Pastikan Anda memiliki Python 3.x terinstal. Unduh dari [python.org](https://www.python.org/).
2. **Instal Library**: Buka Command Prompt dan jalankan perintah:
   ```bash
   pip install pyrogram
   ```
3. **Siapkan Struktur Folder**: Buat folder untuk skrip dan buat folder `media` dan `text`.
4. **Jalankan Skrip**: Buka Command Prompt, arahkan ke direktori skrip, dan jalankan:
   ```bash
   python main.py
   ```

### Linux
1. **Instal Python**: Pastikan Python 3.x terinstal. Gunakan perintah:
   ```bash
   sudo apt-get install python3
   ```
2. **Instal Library**: Jalankan perintah:
   ```bash
   pip3 install pyrogram
   ```
3. **Siapkan Struktur Folder**: Buat folder untuk skrip dan buat folder `media` dan `text`.
4. **Jalankan Skrip**: Buka terminal, arahkan ke direktori skrip, dan jalankan:
   ```bash
   python3 main.py
   ```

### Termux
1. **Instal Python**: Jalankan perintah berikut di Termux:
   ```bash
   pkg install python
   ```
2. **Instal Library**: Jalankan perintah:
   ```bash
   pip install pyrogram
   ```
3. **Siapkan Struktur Folder**: Buat folder untuk skrip dan folder `media` dan `text` di Termux.
4. **Jalankan Skrip**: Arahkan ke direktori skrip dan jalankan:
   ```bash
   python main.py
   ```

## Cara Penggunaan
1. **Konfigurasi `config.json`**: Setelah menjalankan skrip pertama kali, file `config.json` akan dibuat. Isi file ini dengan `api_id`, `api_hash`, `phone_number`, dan delay pengiriman (min dan max).
2. **Menambahkan Saluran**: Edit file `channels.txt` untuk menambahkan saluran yang ingin Anda ikuti.
3. **Menambahkan Media**: Simpan gambar atau video dalam folder `media`.
4. **Menambahkan Teks**: Buat file .txt di folder `text` yang berisi pesan yang ingin dikirim.
5. **Jalankan Skrip**: Setelah semua konfigurasi dilakukan, jalankan skrip dan tunggu pesan terkirim otomatis sesuai pengaturan yang telah ditentukan.

---

Skrip ini adalah alat yang berguna untuk mengelola komunikasi di saluran Telegram secara otomatis. Pastikan untuk mematuhi kebijakan Telegram saat menggunakan skrip ini.
```
