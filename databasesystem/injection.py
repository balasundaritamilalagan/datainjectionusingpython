import sqlite3

# Connect to the database (or create it if not exists)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')

# Sample data
user_data = [
    ('Alice', 'pass123'),
    ('Bob', 'pass456'),
]

# Insert sample data into the table
cursor.executemany('INSERT INTO users (username, password) VALUES (?, ?)', user_data)

# Commit changes and close connection
conn.commit()
conn.close()

# User input (simulate as if it came from a form)
user_input = ("Alice' OR '1'='1", "malicious_password")

# Connect to the database again
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Using parameterized query to prevent SQL injection
query = 'SELECT * FROM users WHERE username = ? AND password = ?'
cursor.execute(query, user_input)

# Fetch the result
result = cursor.fetchone()

# Close the connection
conn.close()

# Check if the result exists
if result:
    print("Login successful.")
else:
    print("Login failed.")
