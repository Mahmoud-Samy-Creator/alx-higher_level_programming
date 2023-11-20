#!/usr/bin/python3

"""
a script that prints the first State object
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Defining connection parameters
user = argv[1]
password = argv[2]
database = argv[3]
host = 'localhost'

if __name__ == "__main__":
    engine = create_engine(f'mysql://{user}:{password}@{host}:3306/{database}')

    # Establishing the connection
    Session = sessionmaker(bind=engine)

    # Session making
    session = Session()

    states = session.query(State).where(State.id == 1).all()

    if states is None:
        print('Nothing')
    else:
        print(states)
