#!/usr/bin/python3

"""
a script that prints the first State object
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    # Establishing the connection
    Session = sessionmaker(bind=engine)

    # Create and update table
    Base.metadata.create_all(engine)

    # Session making
    session = Session()

    # Extract output
    states = session.query(State).order_by(State.id).first()

    # Printing state
    if states is None:
        print('Nothing')
    else:
        print("{}: {}".format(states.id, states.name))

    # Clossing session
    session.close
