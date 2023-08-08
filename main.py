import sqlite3


def create_users_table():
    # Create a connection to the SQLite database
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create a table to store user information
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Insert some sample data into the table
    cursor.execute("INSERT INTO users (username, password) VALUES ('alice', 'password123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('bob', 'qwerty')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('charlie', 'hello123')")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def login_vulnerable(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable SQL query (DO NOT USE THIS IN PRODUCTION!)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)
    user = cursor.fetchone()

    conn.close()

    return user


def login_secure(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Secure SQL query using parameterized query
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    conn.close()

    return user


# Create the 'users' table if it doesn't exist
create_users_table()

# Test the login functions
username = input("Enter your username: ")
password = input("Enter your password: ")

user_vulnerable = login_vulnerable(username, password)
user_secure = login_secure(username, password)

if user_vulnerable:
    print("Vulnerable Login: Login successful!")
else:
    print("Vulnerable Login: Invalid credentials. Login failed.")

if user_secure:
    print("Secure Login: Login successful!")
else:
    print("Secure Login: Invalid credentials. Login failed.")
