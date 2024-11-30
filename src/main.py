from security.encryption import create_token, read_token

from storage.db import check_master_hash, create_database, insert_master_pw


def main():
    db_input_prompt = input("Create new DB (y/n)? ")
    if db_input_prompt == 'y':
        create_database()
    else:
        pass

    

    print("1. Create master password")
    print("2. Continue")
    hashing_option = input("> ")

    if hashing_option == '1':
        insert_master_pw()
    elif hashing_option == '2':
        check_master_hash()

    print("1. Create new password")
    print("2. Get password")
    pw_manager_option = input(">> ")

    if pw_manager_option == '1':
        create_token()
    elif pw_manager_option == '2':
        read_token()

if __name__ == "__main__":
    main()
