from flask import Flask, render_template, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
