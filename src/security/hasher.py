from argon2 import PasswordHasher
# from argon2.exceptions import InvalidHashError, VerifyMismatchError


def create_hash(password):
    # password = input("Create master password: ")
    ph = PasswordHasher()
    salt = input("Create salt: ").encode()
    if salt == b'':
        salt = b'masterpwsalt'

    # with open("hashed.txt", 'w') as file:
    #     file.write(ph.hash(password, salt=salt))
    return ph.hash(password, salt=salt)

# def check_hash(pass_hash, password):
#     ph = PasswordHasher()
#     # with open("hashed.txt", 'r') as file:
#     #     pass_hash = file.readline()
#     try:
#         if ph.verify(pass_hash, password):
#             print("Correct password!")
#     except VerifyMismatchError as e:
#         print("ERROR: ", e)
#         exit(1)
#     except InvalidHashError as e:
#         print("ERROR: ", e)
#         exit(1)
#
#     return password
