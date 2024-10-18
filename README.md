# How to Use

## Command Line Options / Arguments

This script/program supports several argument parameters that can be used. Here's an explanation of the arguments:

### `phone_number` (optional)
This argument is used to specify the phone number for authentication with the Telegram API. It should be in international format, for example: `+621234567890`. This argument is optional; if not provided, it will be read from `config.json`.

**Example:**  
```bash
python main.py +621234567890
```

### `--api API_ID API_HASH` (optional)
This argument is used to provide the API ID and API Hash of your application, which you can obtain from [my.telegram.org](https://my.telegram.org/). This argument is optional and will update the values in `config.json` only if both are provided.

**Example:**  
```bash
python main.py --api 123456 abcdef1234567890abcdef1234567890
```

### `--delay MIN MAX` (optional)
This argument allows you to set the minimum and maximum delay in seconds for the script's actions. If not specified, the default values (30 and 120 seconds) will be used.

**Example:**  
```bash
python main.py --delay 10 60
```

### Example of Full Command
To run the script with a specified phone number, API ID, API Hash, and delay:
```bash
python main.py +621234567890 --api 123456 abcdef1234567890abcdef1234567890 --delay 10 60
```

If you only want to authenticate using the phone number and keep existing configurations:
```bash
python main.py +621234567890
```

### Summary
- Use `phone_number` to authenticate or read it from `config.json`.
- Include `--api` to update both `API_ID` and `API_HASH` in `config.json`.
- Use `--delay` to set the action delay.
- If `API_ID` is provided without `API_HASH`, the change will not be applied.

---

## 📥 Installation

You can download the [**Repository**](https://github.com/username/repo) by cloning it to your system and installing the necessary dependencies. Follow the steps below:


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

5. **Set Up Git for Security**
   To allow Git operations in Termux, run:
   ```bash
   git clone https://github.com/ululazmi18/auto_comment_telegram_channel.git
   cd auto_comment_telegram_channel
   git config --global --add safe.directory /storage/emulated/0/auto_comment_telegram_channel
   ```

---

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

This script is a useful tool for managing communication in Telegram channels automatically. Be sure to comply with Telegram's policies while using this script.
