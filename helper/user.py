import json
    
def login_user(username: str, password: str, users: dict = None):
        
    if username in users and users[username]["password"] == password:
        return users[username]
    return False


def register_user(username: str, password: str, name: str, email: str, users: dict = None):
    
    if username in users:
        return False
    
    users[username] = {
        "name": name,
        "username": username,
        "email": email,
        "password": password
    }

    return users[username], users

def check_user_exists(username: str, users: dict):

    if username in users:
        return True
    return False