import sqlite3


create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
'''

# Step 3: Create a Python Script
# Step 4: Connect to the SQLite database
conn = sqlite3.connect('secure_app.db')
cursor = conn.cursor()

# Step 5: Create the 'users' table
cursor.executescript(create_table_query)

# Step 6: Insert user data into the database (Vulnerable to SQL Injection)
def insert_user_vulnerable(username, password):
    # Split the payload into separate statements
    payload = f"'); DROP TABLE users --"
    statements = payload.split(';')
    
    for statement in statements:
        try:
            cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{statement.strip()}')")
            conn.commit()
        except sqlite3.Error as e:
            print("Error inserting user:", e)

# Step 7: Insert user data into the database (Using Parameterized Query)
def insert_user_secure(username, password):
    query = "INSERT INTO users (username, password) VALUES (?, ?)"
    try:
        cursor.execute(query, (username, password))
        conn.commit()
    except sqlite3.Error as e:
        print("Error inserting user:", e)

# Step 8: Demonstrate SQL Injection (Vulnerable)
print("Vulnerable SQL Injection Example:")
username = "malicious_user"
password = "'); DROP TABLE users --"
insert_user_vulnerable(username, password)
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Step 9: Demonstrate Secure Parameterized Query
print("\nSecure Parameterized Query Example:")
username = "secure_user"
password = "secure_password"
insert_user_secure(username, password)
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Step 10: Close the database connection
conn.close()
