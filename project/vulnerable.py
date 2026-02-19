import sqlite3

def login():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = input("Enter password: ")

    # ✅ FIXED (Safe parameterized query)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))

    results = cursor.fetchall()

    if results:
        print("Login successful")
    else:
        print("Login failed")

login()

