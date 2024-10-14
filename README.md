# 🌟 Telegram Auto Messenger

[![Telegram](https://img.shields.io/badge/Telegram-%40Me-orange)](https://t.me/sho6ot)

![Demo](.github/images/demo.png)

---

## 📜 Keterangan
Skrip ini memungkinkan pengguna untuk **mengirim pesan otomatis** ke saluran Telegram. Pesan yang dikirim dapat menyertakan **media** (gambar atau video) yang disimpan dalam folder `media`. Skrip ini juga secara otomatis bergabung dengan saluran yang diperlukan jika belum terdaftar.

---

## ⚙️ Fungsi
| Fungsionalitas                                                | Didukung |
|-------------------------------------------------------------|:--------:|
| Mengirim pesan teks secara otomatis                          |    ✅    |
| Menyertakan media (gambar atau video) dalam pesan           |    ✅    |
| Bergabung secara otomatis dengan saluran                     |    ✅    |
| Konfigurasi delay antara pengiriman pesan                   |    ✅    |
| Membuat folder dan file konfigurasi secara otomatis          |    ✅    |

---

## 🔧 Pengaturan
| Pengaturan               | Deskripsi                                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**    | Data platform untuk meluncurkan sesi Telegram.                                                                           |
| **PHONE_NUMBER**         | Nomor telepon yang digunakan untuk autentikasi.                                                                          |
| **DELAY_MIN / DELAY_MAX**| Rentang delay dalam detik antara pengiriman pesan.                                                                        |

---

## 📥 Instalasi
Anda dapat mengunduh [**Repository**](https://github.com/username/repo) dengan mengkloningnya ke sistem Anda dan menginstal ketergantungan yang diperlukan. Berikut adalah langkah-langkah terpisah untuk setiap perintah:

### Linux
1. **Clone Repository**
   ```bash
   git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
   ```
   Mengunduh salinan dari repository ke komputer Anda.

2. **Masuk ke Direktori**
   ```bash
   cd auto_comment_telegram_channel
   ```
   Berpindah ke folder yang berisi skrip.

3. **Buat Virtual Environment**
   ```bash
   python3 -m venv venv
   ```
   Membuat lingkungan virtual bernama `venv` untuk mengisolasi dependensi proyek.

4. **Aktifkan Virtual Environment**
   ```bash
   source venv/bin/activate
   ```
   Mengaktifkan lingkungan virtual yang baru saja dibuat.

5. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt
   ```
   Menginstal semua paket yang dibutuhkan yang terdaftar di `requirements.txt`.

6. **Salin File Konfigurasi**
   ```bash
   cp config.json.example config.json
   ```
   Membuat salinan dari file contoh konfigurasi menjadi `config.json`.

7. **Edit File Konfigurasi**
   ```bash
   nano config.json
   ```
   Mengedit file `config.json`. Isi dengan `API_ID`, `API_HASH`, dan `PHONE_NUMBER`.

8. **Jalankan Skrip**
   ```bash
   python3 main.py
   ```
   Menjalankan skrip utama untuk mengaktifkan fitur.

### Windows
1. **Clone Repository**
   ```bash
   git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
   ```
   Mengunduh salinan dari repository ke komputer Anda.

2. **Masuk ke Direktori**
   ```bash
   cd auto_comment_telegram_channel
   ```
   Berpindah ke folder yang berisi skrip.

3. **Buat Virtual Environment**
   ```bash
   python -m venv venv
   ```
   Membuat lingkungan virtual bernama `venv` untuk mengisolasi dependensi proyek.

4. **Aktifkan Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```
   Mengaktifkan lingkungan virtual yang baru saja dibuat.

5. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt
   ```
   Menginstal semua paket yang dibutuhkan yang terdaftar di `requirements.txt`.

6. **Salin File Konfigurasi**
   ```bash
   copy config.json.example config.json
   ```
   Membuat salinan dari file contoh konfigurasi menjadi `config.json`.

7. **Edit File Konfigurasi**
   ```plaintext
   # Isi dengan API_ID, API_HASH, PHONE_NUMBER
   ```
   Buka file `config.json` dan isi dengan informasi yang diperlukan.

8. **Jalankan Skrip**
   ```bash
   python main.py
   ```

---

## 🚀 Cara Penggunaan
1. **Konfigurasi `config.json`**: Setelah menjalankan skrip pertama kali, file `config.json` akan dibuat. Isi file ini dengan `api_id`, `api_hash`, `phone_number`, dan rentang delay pengiriman.
2. **Menambahkan Saluran**: Edit file `channels.txt` untuk menambahkan saluran yang ingin Anda ikuti.
3. **Menambahkan Media**: Simpan gambar atau video dalam folder `media`.
4. **Menambahkan Teks**: Buat file .txt di folder `text` yang berisi pesan yang ingin dikirim.
5. **Jalankan Skrip**: Setelah semua konfigurasi dilakukan, jalankan skrip dan tunggu pesan terkirim otomatis sesuai pengaturan yang telah ditentukan.

---

Skrip ini adalah alat yang berguna untuk mengelola komunikasi di saluran Telegram secara otomatis. Pastikan untuk mematuhi kebijakan Telegram saat menggunakan skrip ini.

--- 
