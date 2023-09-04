import sqlite3

# Step 2: Create a Simple Database
# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

# Insert sample data
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user1', 'password1'))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('user2', 'password2'))

# Commit changes and close the connection
conn.commit()
conn.close()

# Step 3: Perform a Vulnerable Query (Without Parameterization)
username_input = "user1' OR 1=1 --"
password_input = "password"

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Vulnerable query - SQL Injection can occur here!
cursor.execute(f"SELECT * FROM users WHERE username = '{username_input}' AND password = '{password_input}'")

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed")

conn.close()

# Step 4: Mitigate SQL Injection with Parameterized Queries
username_input = "user1' OR 1=1 --"
password_input = "password"

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Use parameterized queries to prevent SQL Injection
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username_input, password_input))

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed")

conn.close()

# Step 5: Explanation
# In a real-world scenario, you should use a more robust authentication system and consider using an ORM library.
