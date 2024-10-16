from pyrogram import Client, types, filters
from datetime import datetime
import re
import asyncio
import os
import json
import random
import logging
import sys

logging.basicConfig(level=logging.ERROR)

# Cek apakah nomor telepon diberikan sebagai argumen
phone_number = sys.argv[1] if len(sys.argv) > 1 else None

config_file = 'config.json'

# Jika config.json belum ada, buat dengan nomor telepon yang diberikan atau kosong
default_config = {
    "api_id": None,
    "api_hash": "",
    "phone_number": phone_number,
    "delay_min": 30,
    "delay_max": 120
}

if not os.path.exists(config_file):
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, indent=4)
    print("File config.json telah dibuat. Silakan isi dengan API ID, Hash, dan delay.")

# Baca config.json yang ada
with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Update nomor telepon jika diberikan sebagai argumen dan berbeda dari yang ada di config.json
if phone_number and config.get('phone_number') != phone_number:
    config['phone_number'] = phone_number
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    print(f"Nomor telepon dalam config.json telah diperbarui menjadi {phone_number}.")
else:
    # Gunakan nomor telepon dari config.json jika tidak diberikan sebagai argumen
    phone_number = config.get('phone_number')

api_id = config.get('api_id')
api_hash = config.get('api_hash')
delay_min = config.get('delay_min', 30)
delay_max = config.get('delay_max', 120)

if api_id is None or api_hash == "" or phone_number == "":
    print("Silakan isi api_id, api_hash, dan phone_number di config.json sebelum menjalankan skrip.")
    exit()

app = Client(phone_number, api_id=api_id, api_hash=api_hash, phone_number=phone_number)

print(f'{datetime.now()}')
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
            if channel.startswith('https://t.me/'):
                channel = extract_channel_username(channel)

            # Langsung mencoba bergabung dengan saluran
            try:
                await app.join_chat(channel)
                # Menambahkan handler untuk pesan
                app.add_handler(app.on_message(filters.chat(channel))(handle_message))
            except Exception:
                # Mengabaikan kesalahan saat bergabung
                pass

        while True:
            await asyncio.sleep(60)

if __name__ == '__main__':
    app.run(main())
