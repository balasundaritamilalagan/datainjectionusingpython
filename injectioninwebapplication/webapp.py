from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create a SQLite database connection
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create a table and insert sample data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT
    )
''')
cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', ('Sample Book', 'John Doe'))
conn.commit()

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        # Perform a search in the database
        cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%' + search_query + '%', '%' + search_query + '%'))
        search_results = cursor.fetchall()
        return render_template('index.html', search_results=search_results)
    return render_template('index.html', search_results=[])

if __name__ == '__main__':
    app.run(debug=True)