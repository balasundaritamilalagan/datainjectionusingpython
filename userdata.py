database={
    "users":{
        "alice": {"password": "pass123", "email": "alice@example.com"},
        "bob":{"password": "pass123", "email": "bob@example.com"},
    }
}

def get_user_data(username):
    query= {"username":username}
    user_data=database["users"][query["username"]]
    return user_data

username_input=input("Enter Username:")
user_data=get_user_data(username_input)
print("User data:", user_data)

def get_user_data_secure(username):
    if username not in database["users"]:
        return None
    user_data=database["users"][username]
    return user_data

username_input= input("Enter Username: ")
user_data = get_user_data_secure(username_input)
if user_data is None:
    print("user not found")
else:
    print("User data:", user_data)