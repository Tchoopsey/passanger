from security.encryption import create_token, read_token
from security.hasher import create_hash, retrieve_hash


def main():
    print("1. Create master password")
    print("2. Continue")
    hashing_option = input("> ")

    if hashing_option == '1':
        create_hash()
    elif hashing_option == '2':
        retrieve_hash()

    print("1. Create new password")
    print("2. Get password")
    pw_manager_option = input(">> ")

    if pw_manager_option == '1':
        create_token()
    elif pw_manager_option == '2':
        read_token()

if __name__ == "__main__":
    main()
