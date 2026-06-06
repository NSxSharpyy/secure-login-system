# 🔐 Secure Login & Authentication System

A highly secure user registration and login web application developed using Python, Flask, and SQLite. This repository demonstrates core web security principles, including secure password handling and safe database querying.

## ⚡ Cyber Security Features Implemented
- **Robust Password Hashing:** Uses the industry-standard `bcrypt` library to securely hash and salt passwords before storing them, protecting user credentials from database leaks.
- **SQL Injection (SQLi) Prevention:** All database operations utilize parametrized queries (parameter binding via `?`), completely neutralizing SQL Injection attack vectors.
- **Secure Session Management:** Leverages Flask's encrypted client-side sessions to maintain user login states securely and destroy tokens immediately upon logout.
- **Concurrency & Reliability:** Configured with specific database access timeouts to handle multiple transaction requests smoothly.

## 🛠️ Tech Stack
- **Backend:** Python 3.x, Flask
- **Database:** SQLite3
- **Security Dependency:** Bcrypt

## 📦 How to Run

1. Clone this repository:
```bash
git clone https://github.com/NSxSharpyy/secure-login-system.git
```
2. Install the necessary packages:
```bash
pip install -r requirements.txt
```
3. Run the development server:
```bash
python app.py
```
4. Open `http://127.0.0.1:5000/register` in your web browser.

## 📝 Server Traffic Logs (Successful Flows)
```text
127.0.0.1 - - "POST /register HTTP/1.1" 200 - (User successfully registered & hashed)
127.0.0.1 - - "GET /login HTTP/1.1" 200 - (Login view loaded)
127.0.0.1 - - "POST /login HTTP/1.1" 302 - (Authentication success, redirecting to dashboard)
127.0.0.1 - - "GET / HTTP/1.1" 200 - (Dashboard securely served via valid active session)
```
