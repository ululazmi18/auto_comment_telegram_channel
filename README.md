<div align="center">

# ⚡ Telegram Channel Auto-Commenter
### *High-Speed Automated Commenting & Channel Engagement Bot for Telegram*

[![Stars](https://img.shields.io/github/stars/ululazmi18/auto_comment_telegram_channel?style=for-the-badge&color=gold)](https://github.com/ululazmi18/auto_comment_telegram_channel/stargazers)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Library](https://img.shields.io/badge/Library-Pyrogram_v2-0088cc?style=for-the-badge&logo=telegram)](https://docs.pyrogram.org/)
[![Termux Ready](https://img.shields.io/badge/Android-Termux_Ready-000000?style=for-the-badge&logo=android)](https://termux.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <a href="#-fitur-utama--key-features">Fitur</a> •
  <a href="#-instalasi--setup">Instalasi</a> •
  <a href="#-konfigurasi--opsi-cli">Konfigurasi</a> •
  <a href="#-panduan-termux-android">Termux Android</a> •
  <a href="#-english-documentation">English Docs</a>
</p>

</div>

---

## 🎯 Gambaran Umum (Overview)

**Telegram Channel Auto-Commenter** adalah bot otomatisasi berbasis **Pyrogram** yang secara otomatis memantau dan mengirimkan komentar interaktif ke setiap postingan baru di channel Telegram yang Anda targetkan. Mendukung lampiran media acak, rotasi teks, pengaturan jeda dinamis (*randomized delay*) untuk mencegah limitasi Telegram, serta kompatibel 100% di **Windows, Linux, dan Android (Termux)**.

---

## 🚀 Fitur Utama (Key Features)

- ⚡ **Deteksi Postingan Baru Real-Time:** Menggunakan event listener Pyrogram untuk merespons postingan seketika saat dipublikasikan.
- 🎲 **Rotasi Pesan & Media Acak:** Mendukung pemilihan teks dari folder `text/` dan gambar/video dari folder `media/` secara acak.
- ⏱️ **Proteksi Anti-Flood & Jeda Dinamis:** Delay acak antar aksi (`--delay min max`) untuk menjaga keamanan akun dari deteksi spam Telegram.
- 🛠️ **Dukungan Konfigurasi Fleksibel:** Atur parameter melalui file `config.json` atau langsung via argumen CLI.
- 📱 **Mobile-First (Termux Compatible):** Didesain ringan agar dapat berjalan 24/7 di ponsel Android menggunakan Termux tanpa memerlukan server mahal.

---

## 📥 Panduan Instalasi (Installation)

### 1. Kloning Repositori
```bash
git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
cd auto_comment_telegram_channel
```

### 2. Instal Dependensi Python
```bash
pip install -r requirements.txt
```

---

## ⚙️ Konfigurasi & Opsi CLI

Anda dapat mengatur kredensial Telegram API melalui file `config.json` atau menyuntikkannya langsung saat eksekusi:

### A. Format `config.json`
```json
{
    "api_id": 12345678,
    "api_hash": "abcdef1234567890abcdef1234567890",
    "phone_number": "+628123456789",
    "delay_min": 30,
    "delay_max": 120
}
```

### B. Argumen Perintah Terminal (CLI Options)

| Argumen | Contoh | Keterangan |
|---|---|---|
| `phone_number` | `+628123456789` | Nomor akun Telegram (format internasional). |
| `--api` | `--api <API_ID> <API_HASH>` | Mendaftarkan API ID & Hash dari [my.telegram.org](https://my.telegram.org). |
| `--delay` | `--delay 15 45` | Menetapkan jeda acak minimum dan maksimum (detik). |

**Contoh Perintah Lengkap:**
```bash
python main.py +628123456789 --api 123456 abcdef1234567890abcdef1234567890 --delay 15 60
```

---

## 📱 Panduan Khusus Termux (Android)

Untuk menjalankan bot ini di latar belakang ponsel Android:

1. **Perbarui dependensi Termux:**
   ```bash
   pkg update && pkg upgrade -y
   pkg install python git -y
   ```
2. **Kloning & Pasang:**
   ```bash
   git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
   cd auto_comment_telegram_channel
   pip install -r requirements.txt
   ```
3. **Jalankan Bot:**
   ```bash
   python main.py
   ```

---

## 🌐 English Documentation

**Telegram Channel Auto-Commenter** is a resilient automation tool built on **Pyrogram** to listen for newly published channel posts and dispatch contextual comments instantly.

- **Real-Time Hook:** Intercepts `on_message` channel events with minimal latency.
- **Spintax & Media Rotation:** Cycles text comments and media attachments randomly.
- **Safety Delay Intervals:** Configurable randomized cooldowns to respect Telegram FloodWait limits.
- **Cross-Platform:** Native support across Windows, macOS, Linux, and Android Termux.

---

## 📄 Lisensi (License)

Didistribusikan di bawah Lisensi **MIT**. Gunakan dengan bijak sesuai dengan Ketentuan Layanan Telegram (Terms of Service). Dibuat oleh [**Ulul Azmi**](https://github.com/ululazmi18).
