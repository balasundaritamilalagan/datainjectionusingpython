import secrets

from flask import session


def generate_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(16);
        # session['mytoken']='3d6f45a5fc12445dbac2f59c3b6c7cb1';
    return session['csrf_token']

def validate_csrf_token(request_token):
    session_token = session.get('csrf_token')
    if session_token is None or session_token != request_token:
        return False
    return True
