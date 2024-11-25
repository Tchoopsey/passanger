from cryptography.fernet import Fernet
import base64


def create_token():
    with open('hashed.txt', 'r') as file:
        # create 32 url safe base64 encoded key for Fernet
        # out of the master password hash
        key = base64.urlsafe_b64encode(file.readline()[:32].encode())

    f = Fernet(key)

    password = input("Enter password: ").encode()
    token = f.encrypt(password)
    with open("password.txt", 'w') as file:
        file.write(token.decode())

def read_token():
    with open('hashed.txt', 'r') as file:
        key = file.readline()
        key = base64.urlsafe_b64encode(key[:32].encode())

    f = Fernet(key)

    with open("password.txt", 'r') as file:
        token = file.readline()
        password = f.decrypt(token)
        print(password.decode())
