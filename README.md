Sure! Here’s the updated installation section without "All Systems":

---

## 📥 Installation

You can download the [**Repository**](https://github.com/username/repo) by cloning it to your system and installing the necessary dependencies. Follow the steps below:

1. **Clone Repository**
   ```bash
   git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
   ```
   Downloads a copy of the repository to your computer.

2. **Navigate to Directory**
   ```bash
   cd auto_comment_telegram_channel
   ```
   Moves to the folder containing the script.

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Installs all required packages listed in `requirements.txt`.

4. **Edit Configuration File**
   ```bash
   nano config.json
   ```
   Fill it with `API_ID`, `API_HASH`, and `PHONE_NUMBER`.

5. **Run the Script**
   ```bash
   python main.py
   ```
   Executes the main script to activate the features.

---

### Additional Steps for Termux

1. **Update Packages**
   ```bash
   pkg update && pkg upgrade
   ```

2. **Install Required Packages**
   ```bash
   pkg install python git
   ```

3. **Allow Storage Access**
   Run the following command to grant storage access:
   ```bash
   termux-setup-storage
   ```
   Select "Allow" when prompted.

4. **Access Internal Folder**
   ```bash
   cd /storage/emulated/0
   ```

---

## 🚀 How to Use
1. **Configure `config.json`**: After running the script for the first time, fill this file with `api_id`, `api_hash`, `phone_number`, and the delay range for sending messages.
2. **Add Channels**: Edit the `channels.txt` file to add the channels you want to follow.
3. **Add Media**: Save images or videos in the `media` folder.
4. **Add Text**: Create a .txt file in the `text` folder containing the messages you want to send.
5. **Run the Script**: Once all configurations are done, run the script and wait for the messages to be sent automatically as per the specified settings.

---

This script is a useful tool for managing communication in Telegram channels automatically. Be sure to comply with Telegram's policies while using this script.

---
