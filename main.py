import argparse
from pyrogram import Client, types, filters
from datetime import datetime
import re
import asyncio
import os
import json
import random
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.ERROR)

# Setup argparser
parser = argparse.ArgumentParser(description='Skrip Auto Comment Telegram')
parser.add_argument('phone_number', nargs='?', help='Nomor telepon untuk akun Telegram')
parser.add_argument('--api', nargs=2, metavar=('API_ID', 'API_HASH'), help='API ID dan API Hash untuk Telegram')
parser.add_argument('--delay', nargs=2, type=int, metavar=('MIN', 'MAX'), help='Delay minimum dan maksimum dalam detik')

args = parser.parse_args()

# Ambil argumen dari parser
phone_number = args.phone_number
api_id = args.api[0] if args.api else None
api_hash = args.api[1] if args.api else ""
delay_min = args.delay[0] if args.delay else 30
delay_max = args.delay[1] if args.delay else 120

config_file = 'config.json'

# Jika config.json belum ada, buat dengan default
default_config = {
    "api_id": None,
    "api_hash": "",
    "phone_number": phone_number,
    "delay_min": delay_min,
    "delay_max": delay_max
}

if not os.path.exists(config_file):
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, indent=4)
    print("File config.json telah dibuat. Silakan isi dengan API ID, Hash, dan delay. atau dengan")
    print("python main.py +621234567890 --api 123456 abcdef1234567890abcdef1234567890 --delay 10 60")

# Baca config.json yang ada
with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Jika phone_number tidak diberikan sebagai argumen, ambil dari config.json
if phone_number is None:
    phone_number = config.get('phone_number')

# Validasi phone_number
if phone_number is None:
    print("Error: phone_number harus diberikan sebagai argumen atau ada dalam config.json.")
    exit()

# Update config jika argumen diberikan
if args.phone_number:
    config['phone_number'] = phone_number
if api_hash and api_id is not None:  # Hanya jika api_hash dan api_id diberikan
    config['api_id'] = int(api_id)  # Pastikan api_id adalah integer
    config['api_hash'] = api_hash
if args.delay:
    config['delay_min'] = delay_min
    config['delay_max'] = delay_max

# Simpan perubahan pada config.json
with open(config_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4)

# Ambil nilai dari config
api_id = config.get('api_id')
api_hash = config.get('api_hash')

if api_id is None or api_hash == "":
    print("Silakan isi api_id, api_hash, dan phone_number di config.json sebelum menjalankan skrip. atau dengan")
    print("python main.py +621234567890 --api 123456 abcdef1234567890abcdef1234567890 --delay 10 60")
    exit()

app = Client(phone_number, api_id=api_id, api_hash=api_hash)

print(f'{datetime.now()} ({phone_number})')
print(f'Aplikasi auto komen sudah aktif.')

os.makedirs('text', exist_ok=True)

default_channels = "test13524\nayayawae15243"

if not os.path.exists('channels.txt'):
    with open('channels.txt', 'w', encoding='utf-8') as channels_file:
        channels_file.write(default_channels)
        print("File channels.txt telah dibuat dengan isi default.")

with open('channels.txt', 'r') as file:
    target_channels = [line.strip() for line in file if line.strip()]

async def countdown(t):
    for i in range(t, 0, -1):
        minute, seconds = divmod(i, 60)
        hour, minute = divmod(minute, 60)
        seconds = str(seconds).zfill(2)
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        print(f"wait - {hour}:{minute}:{seconds}", flush=True, end="\r")
        await asyncio.sleep(1)

async def handle_message(client, message: types.Message):
    delay = random.randint(delay_min, delay_max)
    dm = await client.get_discussion_message(message.chat.id, message.id)

    text_files = [f for f in os.listdir('text') if f.endswith('.txt')]
    if text_files:
        random_text_file = random.choice(text_files)
        with open(os.path.join('text', random_text_file), 'r', encoding='utf-8') as text_file:
            message_text = text_file.read().strip()
    else:
        message_text = "Tidak ada teks untuk dikirim."

    media_files = [f for f in os.listdir('media') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.avi'))]

    channel_name = message.chat.title or message.chat.username or message.chat.id

    if media_files:
        media_file = random.choice(media_files)
        media_path = os.path.join('media', media_file)
        await countdown(delay)
        try:
            if media_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                await dm.reply_photo(photo=media_path, caption=message_text)
                print(f'Text + Photo Terkirim ke {channel_name}')
            elif media_path.lower().endswith(('.mp4', '.avi')):
                await dm.reply_video(video=media_path, caption=message_text)
                print(f'Text + Video Terkirim ke {channel_name}')
        except Exception:
            # Mengabaikan kesalahan ketika tidak bisa mengirim
            pass
    else:
        await countdown(delay)
        await dm.reply(message_text)
        print(f'Text Terkirim ke {channel_name}')

def extract_channel_username(url):
    pattern = r't.me/(joinchat/)?(?P<username>[^/?]+)'
    match = re.search(pattern, url)
    return match.group('username') if match else None
    
async def main():
    async with app:
        for channel in target_channels:
            app.add_handler(app.on_message(filters.chat(channel))(handle_message))

        while True:
            await asyncio.sleep(60)

if __name__ == '__main__':
    app.run(main())
