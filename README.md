# Telegram Auto Messenger

[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/sho6ot)

![img1](.github/images/demo.png)

## Keterangan
Skrip ini memungkinkan pengguna untuk mengirim pesan otomatis ke saluran Telegram. Pesan yang dikirim dapat menyertakan media (gambar atau video) yang disimpan dalam folder `media`. Skrip ini juga secara otomatis bergabung dengan saluran yang diperlukan jika belum terdaftar.

## Fungsi
| Fungsionalitas                                                | Didukung |
|-------------------------------------------------------------|:--------:|
| Mengirim pesan teks secara otomatis                          |    ✅    |
| Menyertakan media (gambar atau video) dalam pesan           |    ✅    |
| Bergabung secara otomatis dengan saluran                     |    ✅    |
| Konfigurasi delay antara pengiriman pesan                   |    ✅    |
| Membuat folder dan file konfigurasi secara otomatis          |    ✅    |

## Pengaturan
| Pengaturan               | Deskripsi                                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**    | Data platform untuk meluncurkan sesi Telegram.                                                                           |
| **PHONE_NUMBER**         | Nomor telepon yang digunakan untuk autentikasi.                                                                          |
| **DELAY_MIN / DELAY_MAX**| Rentang delay dalam detik antara pengiriman pesan.                                                                        |

## Instalasi
Anda dapat mengunduh [**Repository**](https://github.com/username/repo) dengan mengkloningnya ke sistem Anda dan menginstal ketergantungan yang diperlukan:

```shell
# Linux
~ >>> git clone https://github.com/username/repo.git
~ >>> cd repo
~ >>> python3 -m venv venv
~ >>> source venv/bin/activate
~ >>> pip install -r requirements.txt
~ >>> cp config.json.example config.json
~ >>> nano config.json # Isi dengan API_ID, API_HASH, PHONE_NUMBER
~ >>> python3 main.py

# Windows
~ >>> git clone https://github.com/username/repo.git
~ >>> cd repo
~ >>> python -m venv venv
~ >>> venv\Scripts\activate
~ >>> pip install -r requirements.txt
~ >>> copy config.json.example config.json
~ >>> # Isi dengan API_ID, API_HASH, PHONE_NUMBER
~ >>> python main.py
