import random
import string

# Global dictionary to simulate a database for storing session data
sessions = {}

# Function to generate a random session ID
def generate_session_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

# Function to create a new session for a user
def create_session(user_id):
    session_id = generate_session_id()
    sessions[session_id] = {'user_id': user_id}
    return session_id

# Function to validate a session
def validate_session(session_id, user_id):
    if session_id in sessions and sessions[session_id]['user_id'] == user_id:
        return True
    return False

# Function to prevent session hijacking by using user agent and IP checks
def prevent_hijacking(session_id, user_agent, user_ip):
    if session_id in sessions:
        session_data = sessions[session_id]
        if session_data['user_agent'] == user_agent and session_data['user_ip'] == user_ip:
            return True
    return False

# Function to simulate user login and session creation
def login(user_id, user_agent, user_ip):
    session_id = create_session(user_id)
    session_data = sessions[session_id]
    session_data['user_agent'] = user_agent
    session_data['user_ip'] = user_ip
    return session_id

# Simulate user login and session creation
user_id = "12345"
user_agent = "Mozilla/5.0"
user_ip = "192.168.1.1"
session_id = login(user_id, user_agent, user_ip)

# Simulate session validation and prevention of session hijacking
if validate_session(session_id, user_id):
    print("Session is valid.")
    if prevent_hijacking(session_id, user_agent, user_ip):
        print("Session hijacking prevented.")
    else:
        print("Session hijacking detected.")
else:
    print("Invalid session.")
