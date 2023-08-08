import sqlite3

# Create the database and table
def create_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Create a new user
def create_user(username, password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Use parameterized query to insert user data
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

    conn.commit()
    conn.close()

# Fetch all users' information
def fetch_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Fetch and return user data
    cursor.execute('SELECT id, username FROM users')
    users = cursor.fetchall()

    conn.close()
    return users

if __name__ == '__main__':
    create_database()

    create_user('alice', 'securepassword123')
    create_user('bob', 'anothersecurepassword456')

    users = fetch_users()
    for user in users:
        print(f"User ID: {user[0]}, Username: {user[1]}")
