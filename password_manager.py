""" the point of this program is to kind of organize and
store your passwords so we're going to store all of the
passwords along with the username or the account
they're associated in a text file """
from cryptography.fernet import Fernet
"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account name: ")
    pwd = input("Account password: ")

    with open('passwords.txt', 'a+') as f:
        f.seek(0)
        first_char = f.read(1)
        if not first_char:
            f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}")
        else:
            f.write(f"\n{name}|{fer.encrypt(pwd.encode()).decode()}")

while True:
    mode = input("Would you like to add a new password or view existing one? (view, add), press q to quit.").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

