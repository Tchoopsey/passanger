from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def create_hash():
    password = input("Create master password: ")
    ph = PasswordHasher()
    salt = input("Create salt: ").encode()
    if salt == b'':
        salt = b'masterpwsalt'

    with open("hashed.txt", 'w') as file:
        file.write(ph.hash(password, salt=salt))

def retrieve_hash():
    password = input("Password: ")
    ph = PasswordHasher()
    with open("hashed.txt", 'r') as file:
        pass_hash = file.readline()
        try:
            if ph.verify(pass_hash, password):
                print("Correct password!")
        except VerifyMismatchError as e:
            print("ERROR: ", e)
            exit(1)
