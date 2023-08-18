import requests
from bs4 import BeautifulSoup

def unsafe_input_function(input_data):
    return "you entered: "+input_data

def test_sql_injection():
    malicious_input="'; DROP TABLE users; --"
    response=unsafe_input_function(malicious_input)

    if "DROP TABLE" in response:
        print("SQL Injection vulnerability detected!")
    else:
        print("No SQL injection vulnerablitiy detected!")
test_sql_injection()
