from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base

def create_database():
    db_name = input('Enter database name: ')
    engine = create_engine(f'sqlite:///{db_name}.db', echo=True)
    Base.metadata.create_all(engine)

create_database()
