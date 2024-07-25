import sqlite3
import hashlib

def setup_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    except sqlite3.IntegrityError:
        print(f"User {username} already exists.")
    conn.commit()
    conn.close()

setup_database()
add_user("Tanisha", "Tanisha49")

import sqlite3
import hashlib

def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    
    if result:
        stored_password = result[0]
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        if hashed_password == stored_password:
            return "Login successful!"
        else:
            return "Login failed. Incorrect password."
    else:
        return "Login failed. Username not found."

username = input("Enter your username: ")
password = input("Enter your password: ")
result = authenticate(username, password)
print(result)

