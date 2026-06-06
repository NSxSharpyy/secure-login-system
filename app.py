import sqlite3
# 🟢 Ise copy karke replace karein (url_location ki jagah url_for aayega):
from flask import Flask, render_template, request, redirect, session, url_for
import bcrypt

app = Flask(__name__)
# Secret key session ko secure (encrypt) rakhne ke liye zaroori hai
app.secret_key = "super_secret_cybersecurity_key_change_this_later"

# Database initialization (Database aur Table banana)
def init_db():
    conn = sqlite3.connect("users.db",timeout=10)
    cursor = conn.cursor()
    # Table banao agar pehle se nahi bani hai
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 1. HOME ROUTE (Dashboard)
@app.route('/')
def home():
    # Check karo kya user logged in hai (Session Check)
    if 'username' in session:
        return f"<h1>Welcome to the Dashboard, {session['username']}! 👋</h1><br><a href='/logout'>Logout</a>"
    return redirect('/login')

# 2. USER REGISTRATION (Locker Banana)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        
        # Simple Input Validation
        if not username or not password:
            return "Username and Password cannot be empty!"

        # Password ko Hash karna (Bcrypt Jadoo)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        try:
            conn = sqlite3.connect("users.db",timeout=10)
            cursor = conn.cursor()
            # Security: Using '?' prevents SQL Injection entirely
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            conn.close()
            return "Registration Successful! <a href='/login'>Login here</a>"
        except sqlite3.IntegrityError:
            return "Username already exists! Try another one."
            
    return render_template('register.html')

# 3. USER LOGIN (Verification)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        conn = sqlite3.connect("users.db",timeout=10)
        cursor = conn.cursor()
        # Secure search using parameter binding
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user:
            db_password = user[0]
            # Bcrypt se plaintext password aur hashed password ko compare karna
            if bcrypt.checkpw(password.encode('utf-8'), db_password):
                # Session ke andar token store karna (Session Management)
                session['username'] = username
                return redirect('/')
            
        return "Invalid Username or Password! ❌"

    return render_template('login.html')

# 4. LOGOUT (Session Token Delete Karna)
@app.route('/logout')
def logout():
    session.pop('username', None) # Token delete kar do
    return "Logged out successfully! <a href='/login'>Login again</a>"

if __name__ == '__main__':
    init_db() # Run hone se pehle DB banao
    app.run(debug=True)
