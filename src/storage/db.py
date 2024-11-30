from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from .models import Base, MasterPassword, ServicePasswords

from security.hasher import create_hash, check_hash 

def create_database():
    db_name = input('Enter database name: ')
    engine = create_engine(f'sqlite:///{db_name}.db', echo=True)
    Base.metadata.create_all(engine)

def insert_master_pw():
    password = input("Create master password: ")
    master_pw = create_hash(password) 
    print(master_pw)
    engine = create_engine(f'sqlite:///password.db', echo=True)
    with Session(engine) as session:
        new_master = MasterPassword(
            master_password=master_pw
        )
        session.add(new_master)
        session.commit()

def check_master_hash():
    # __import__('pdb').set_trace()
    password = input("Password: ")
    password = create_hash(password)
    engine = create_engine(f'sqlite:///password.db', echo=True)
    with Session(engine) as session:
        try:
            master_pw = session.query(MasterPassword).first().master_password
            print(password)
            print(master_pw)
        except NoResultFound as e:
            print(e)
            exit(1)

    if password == master_pw:
        print("Correct!")
        return master_pw
    else:
        print("Incorrect password!")
        exit(1)
