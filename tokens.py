import json
import random

def get():
    with open("users.json") as file:
        return json.load(file)

def update(dic):
    with open("users.json","w") as file:
        json.dump(dic,file,indent=4)

def check(token:str):
    users = get()
    if not token: return False

    for user in users:
        if users[user]["token"] == token: return user
    else: return False

def check_login(user,password):
    users = get()
    if user in users:
        if users[user]["password"] == password:
            return True
    return False

def gen():
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = list("abcdefghijklmnopqrstuvwxyz")
    digit = list("1234567890")
    def string():
        return "".join(random.choices(upper+lower+digit,k=10))
    while 1:
        token = string()+"-"+string()+"-"+string()+"-"+string()+"-"+string()
        users = get()
        for user in users:
            if token == users[user]["token"] == token:
                pass
        else:
            return token

def add(user,password):
    token = gen()
    users = get()
    users[user] = {"password":password,"token":token}
    update(users)

def update_user(username):
    token = gen()
    users = get()
    users[username]["token"] = token
    update(users)