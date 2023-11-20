#!/usr/bin/python3

"""
a script that prints the first State object
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Establishing the connection
    Session = sessionmaker(bind=engine)

    # Session making
    session = Session()

    states = session.query(State).order_by(State.id).first()

    # Printing state
    if states is None:
        print('Nothing')
    else:
        print(states)

    # Clossing session
    session.close
