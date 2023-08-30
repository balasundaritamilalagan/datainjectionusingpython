from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import re

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Whitelist of acceptable usernames
whitelist_usernames = ["Alice", "bobmarleydj", "charliechaplin"]  # Add more usernames as needed

# Validate username and password format using regular expressions
def is_valid_username(username):
    # Add your username format validation logic here
    return len(username) >=8& username[0].isupper() and not any(char.isspace() for char in username)

def is_valid_password(password):
    # Add your password format validation logic here
    return len(password) >= 8  # For example, require a minimum length of 8 characters

# Implement Secure Coding Practices

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Secure Coding Practice: Input Validation
        if not username or not password:
            error = "Both username and password are required."
        elif not is_valid_username(username):
            error = "Invalid username format."
        elif not is_valid_password(password):
            error = "Invalid password format. Password must be at least 8 characters long."
        elif username not in whitelist_usernames:
            error = "Username not in whitelist of acceptable usernames."
        else:
            # Secure Coding Practice: Use Parameterized Queries
            db.users.insert_one({"username": username, "password": password})
            return redirect(url_for("success"))
    else:
        error = None
    return render_template("index.html", error=error)

@app.route("/success")
def success():
    return "User data inserted successfully."

if __name__ == "__main__":
    app.run(debug=True)
