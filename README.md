# How to Use

## Command Line Options / Arguments

This script/program supports several argument parameters that can be used. Here's an explanation of the arguments:

### `phone_number` (required)
This argument is used to specify the phone number for authentication with the Telegram API. It should be in international format, for example: `+621234567890`. This is a mandatory argument for the script to function correctly.

**Example:**  
```bash
python main.py +621234567890
```

### `api_id` (optional)
This argument is used to provide the API ID of your application, which you can obtain from [my.telegram.org](https://my.telegram.org/). It is optional and will only be used if `api_hash` is also provided. If included, it will update the value in `config.json`.

**Example:**  
```bash
python main.py +621234567890 123456
```

### `api_hash` (optional)
This argument is used to provide the API Hash of your application, which you also get from Telegram. This is required if you wish to update `api_id` in `config.json`. If `api_hash` is not provided, any specified `api_id` will be ignored, and `config.json` will remain unchanged.

**Example:**  
```bash
python main.py +621234567890 123456 abcdef1234567890abcdef1234567890
```

### Example of Full Command
To authenticate and update both `api_id` and `api_hash`, you would run:
```bash
python main.py +621234567890 123456 abcdef1234567890abcdef1234567890
```

If you only want to authenticate using the phone number and keep existing configurations, you can run:
```bash
python main.py +621234567890
```

### Summary
- Use `phone_number` to authenticate.
- Include `api_id` and `api_hash` if you want to update these values in `config.json`.
- If only `api_id` is provided without `api_hash`, it will be ignored, and no changes will be made.

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

This script is a useful tool for managing communication in Telegram channels automatically. Be sure to comply with Telegram's policies while using this script.

---
