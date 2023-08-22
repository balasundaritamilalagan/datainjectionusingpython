from flask import render_template, request

from CSRF.app import app
from CSRF.secrets import validate_csrf_token, generate_csrf_token


@app.route('/')
def index():
    return render_template('index.html', csrf_token=generate_csrf_token())

@app.route('/process', methods=['POST'])
def process():
    request_token = request.form.get('csrf_token')
    if validate_csrf_token(request_token):
        # Process the form data
        return "Form processed successfully!"
    else:
        return "CSRF token validation failed."
