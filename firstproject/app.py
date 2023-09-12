import os
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory list to store data
data_list = []

@app.route('/')
def index():
    return render_template('upload.html', data=data_list)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        # List of encodings to try
        encodings_to_try = ['utf-8', 'utf-16', 'latin1', 'ISO-8859-1', 'cp1252']

        for encoding in encodings_to_try:
            try:
                data = pd.read_csv(file, encoding=encoding)
                for index, row in data.iterrows():
                    entry = {'name': row['name']}
                    data_list.append(entry)
                return redirect(url_for('index'))
            except UnicodeDecodeError:
                continue

        # If none of the encodings worked, return an error
        return "Error: Unable to decode the CSV file with any of the specified encodings."

if __name__ == '__main__':
    app.run(debug=True)
