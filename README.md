
# 🔐 Password Manager (Python + Tkinter)

A simple **Password Manager desktop application** built using **Python and Tkinter**.
It helps users generate strong passwords and securely save website login details to a local file.

---

## ✨ Features

* Generate strong random passwords
* Automatically copy generated password to clipboard
* Save website, email/username, and password
* User-friendly GUI using Tkinter
* Data stored locally in a text file

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* `random` module
* `pyperclip` (clipboard support)

---

## 📂 Project Structure

```
├── main.py                 # Main GUI application
├── password_generator.py   # Password generation logic
├── save_password.py        # Save password to file
├── password_data.txt       # Stores saved credentials
├── logo.png                # App logo
```

---

## ▶️ How to Run

1. Install required dependency:

   ```bash
   pip install pyperclip
   ```

2. Run the application:

   ```bash
   python main.py
   ```

---

## 🧠 How It Works

* **Generate Password**: Creates a random password with letters, numbers, and symbols.
* **Add Button**: Saves entered details after user confirmation.
* Passwords are stored in `password_data.txt`.

---

## 📌 Notes

* This project is for **learning purposes**.
* Passwords are saved in **plain text**, not encrypted.

---

## 👤 Author

**Upendra Uddagiri**
Computer Science Student

---



Just tell me 👍
