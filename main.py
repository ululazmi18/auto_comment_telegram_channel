from pyrogram import Client, types, filters
from datetime import datetime
import re
from pyrogram.errors.exceptions.forbidden_403 import Forbidden
import asyncio
import os
import json
import random
import logging

logging.basicConfig(level=logging.ERROR)

print("Skrip ini memungkinkan Anda mengirim pesan otomatis ke saluran Telegram.")
print("Simpan media (gambar atau video) dalam folder 'media' untuk menyertakan dalam pesan.")
print("Jika folder 'media' belum ada, skrip ini akan membuatnya secara otomatis.")
print("File 'config.json' akan dibuat jika belum ada. Isikan dengan API ID, Hash Telegram, nomor telepon, dan delay pengiriman.")
print("Folder 'text' akan dibuat jika belum ada, berisi file .txt yang akan dikirim secara acak.")
print("File 'channels.txt' akan dibuat jika belum ada, berisi daftar saluran yang akan diikuti.")
print("Pastikan untuk mengisi 'config.json' dengan informasi yang diperlukan sebelum menjalankan skrip.")
print("Skrip ini juga akan secara otomatis bergabung dengan saluran yang diperlukan jika belum terdaftar.")

config_file = 'config.json'

default_config = {
    "api_id": None,  
    "api_hash": "",  
    "phone_number": "",  
    "delay_min": 30,  
    "delay_max": 120  
}

if not os.path.exists(config_file):
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, indent=4)
    print("File config.json telah dibuat. Silakan isi dengan API ID, Hash, nomor telepon, dan delay.")

with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

api_id = config.get('api_id')
api_hash = config.get('api_hash')
phone_number = config.get('phone_number')
delay_min = config.get('delay_min', 30)
delay_max = config.get('delay_max', 120)

if api_id is None or api_hash == "" or phone_number == "":
    print("Silakan isi api_id, api_hash, dan phone_number di config.json sebelum menjalankan skrip.")
    exit()

app = Client(phone_number, api_id=api_id, api_hash=api_hash)

print(f'{datetime.now()}')
print(f'aplikasi auto komen berhasil dijalankan untuk channels: ')

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

async def is_subscribed(client, channel):
    try:
        member = await client.get_chat_member(channel, 'me')
        return member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f'Gagal memeriksa status langganan di {channel}: {e}')
        return False
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
        except Forbidden:
            await dm.chat.join()
            if media_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                await dm.reply_photo(photo=media_path, caption=message_text)
                print(f'Text + Photo Terkirim ke {channel_name}')
            elif media_path.lower().endswith(('.mp4', '.avi')):
                await dm.reply_video(video=media_path, caption=message_text)
                print(f'Text + Video Terkirim ke {channel_name}')
    else:
        await countdown(delay)
        await dm.reply(message_text)
        print(f'Text Terkirim ke {channel_name}')

    await asyncio.sleep(180)

def extract_channel_username(url):
    pattern = r't.me/(joinchat/)?(?P<username>[^/?]+)'
    match = re.search(pattern, url)
    return match.group('username') if match else None

async def main():
    async with app:
        for channel in target_channels:
            if channel.startswith('https://t.me/'):
                channel = extract_channel_username(channel)
            if not await is_subscribed(app, channel):
                try:
                    await app.join_chat(channel)
                    print(f'-{channel}')
                except Exception as e:
                    print(f'Gagal bergabung dengan saluran {channel}: {e}')
                    continue
            app.add_handler(
                app.on_message(filters.chat(channel))(handle_message)
            )

        while True:
            await asyncio.sleep(60)

if __name__ == '__main__':
    app.run(main())
