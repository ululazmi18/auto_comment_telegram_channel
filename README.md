# 🌟 Telegram Auto Messenger

---

## 📜 Description
This script allows users to **send automated messages** to Telegram channels. The sent messages can include **media** (images or videos) stored in a `media` folder. The script also automatically joins the necessary channels if not already a member.

---

## ⚙️ Features
| Functionality                                                | Supported |
|-------------------------------------------------------------|:--------:|
| Automatically send text messages                             |    ✅    |
| Include media (images or videos) in messages                |    ✅    |
| Automatically join channels                                   |    ✅    |
| Configure delay between message sends                        |    ✅    |
| Automatically create configuration folder and files          |    ✅    |

---

## 🔧 Settings
| Setting                 | Description                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**   | Platform data to initiate a Telegram session.                                                                               |
| **PHONE_NUMBER**        | The phone number used for authentication.                                                                                    |
| **DELAY_MIN / DELAY_MAX**| Range of delay in seconds between sending messages.                                                                          |

---

## 📥 Installation
You can download the [**Repository**](https://github.com/username/repo) by cloning it to your system and installing the necessary dependencies. Here are the separate steps for each command:

---
### Linux
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

3. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   ```
   Creates a virtual environment named `venv` to isolate project dependencies.

4. **Activate Virtual Environment**
   ```bash
   source venv/bin/activate
   ```
   Activates the newly created virtual environment.

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Installs all required packages listed in `requirements.txt`.

6. **Copy Configuration File**
   ```bash
   cp config.json.example config.json
   ```
   Creates a copy of the example configuration file named `config.json`.

7. **Edit Configuration File**
   ```bash
   nano config.json
   ```
   Edits the `config.json` file. Fill it with `API_ID`, `API_HASH`, and `PHONE_NUMBER`.

8. **Run the Script**
   ```bash
   python3 main.py
   ```
   Executes the main script to activate the features.

---
### Windows
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

3. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```
   Creates a virtual environment named `venv` to isolate project dependencies.

4. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```
   Activates the newly created virtual environment.

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Installs all required packages listed in `requirements.txt`.

6. **Copy Configuration File**
   ```bash
   copy config.json.example config.json
   ```
   Creates a copy of the example configuration file named `config.json`.

7. **Edit Configuration File**
   ```plaintext
   # Fill in with API_ID, API_HASH, PHONE_NUMBER
   ```
   Open the `config.json` file and fill it with the required information.

8. **Run the Script**
   ```bash
   python main.py
   ```
Here's the English version of your instructions:

---
### Termux

1. **Update Packages**
   ```bash
   pkg update && pkg upgrade
   ```

2. **Allow Storage Access**
   Run the following command to grant storage access:
   ```bash
   termux-setup-storage
   ```
   After running this command, select "Allow" when prompted.

3. **Access Internal Folder**
   To access the internal folder, use the following command:
   ```bash
   cd /storage/emulated/0
   ```

4. **Install Required Packages**
   ```bash
   pkg install python git
   ```

5. **Clone Repository**
   ```bash
   git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
   ```
   This will download a copy of the repository to your device.

6. **Navigate to the Directory**
   ```bash
   cd auto_comment_telegram_channel
   ```

7. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

8. **Activate the Virtual Environment**
   ```bash
   source venv/bin/activate
   ```

9. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

10. **Copy Configuration File**
    ```bash
    cp config.json.example config.json
    ```

11. **Edit Configuration File**
    ```bash
    nano config.json
    ```
    Fill in with `API_ID`, `API_HASH`, and `PHONE_NUMBER`.

12. **Run the Script**
    ```bash
    python main.py
    ```

---
## 🚀 How to Use
1. **Configure `config.json`**: After running the script for the first time, the `config.json` file will be created. Fill this file with `api_id`, `api_hash`, `phone_number`, and the delay range for sending messages.
2. **Add Channels**: Edit the `channels.txt` file to add the channels you want to follow.
3. **Add Media**: Save images or videos in the `media` folder.
4. **Add Text**: Create a .txt file in the `text` folder containing the messages you want to send.
5. **Run the Script**: Once all configurations are done, run the script and wait for the messages to be sent automatically as per the specified settings.

---

This script is a useful tool for managing communication in Telegram channels automatically. Be sure to comply with Telegram's policies while using this script.

---
