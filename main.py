import sqlite3

# Step 1: Connect to the database (or create one if it doesn't exist)
conn = sqlite3.connect("users.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Define the SQL command to create the 'users' table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

# Step 4: Execute the SQL command to create the 'users' table
cursor.execute(create_table_query)

# Step 5: Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'users.db' and table 'users' created successfully!")
import sqlite3

def create_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Safe way to execute a SQL query using parameters
    insert_query = "INSERT INTO users (username, password) VALUES (?, ?)"
    cursor.execute(insert_query, (username, password))

    conn.commit()
    conn.close()

def main():
    print("Welcome to the user registration system!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    create_user(username, password)
    print("User registration successful!")

if __name__ == "__main__":
    main()