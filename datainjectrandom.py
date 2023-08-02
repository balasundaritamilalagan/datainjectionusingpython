import sqlite3
import random

# Create a connection to the database (it will create a new database if it doesn't exist)
conn = sqlite3.connect('data_injection_example.db')
cursor = conn.cursor()

# Create a table for users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()


# Step 4: Data Injection Function
def inject_random_data(num_records):
    # Open a connection to the database
    conn = sqlite3.connect('data_injection_example.db')
    cursor = conn.cursor()

    # List of names, ages, and email domains for random data generation
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
    ages = range(18, 61)
    email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']

    # Inject random data into the table
    for _ in range(num_records):
        name = random.choice(names)
        age = random.choice(ages)
        email = f'{name.lower()}_{random.randint(100, 999)}@{random.choice(email_domains)}'

        # Execute the SQL INSERT command
        cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)', (name, age, email))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# Step 5: Data Injection
inject_random_data(10)


# Step 6: Retrieving and Displaying Injected Data
def fetch_data():
    # Open a connection to the database
    conn = sqlite3.connect('data_injection_example.db')
    cursor = conn.cursor()

    # Fetch all records from the users table
    cursor.execute('SELECT * FROM users')
    records = cursor.fetchall()

    # Display the fetched data
    for record in records:
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3]}")

    # Close the connection
    conn.close()


# Step 7: Display Injected Data
fetch_data()
