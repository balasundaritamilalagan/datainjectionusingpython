from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Create the 'users' table and insert a user record during setup
def setup_database():
    conn = sqlite3.connect('user_db.db')
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Insert a user record if the table is newly created
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    if user_count == 0:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('testuser', 'testpassword'))
        conn.commit()

    conn.close()

@app.route('/')
def index():
    return render_template('log.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('user_db.db')
    cursor = conn.cursor()

    # Prevent SQL injection using parameterized query
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        return "Login successful!"
    else:
        return "Login failed."

if __name__ == '__main__':
    setup_database()  # Call the setup function before running the app
    app.run(debug=True)
