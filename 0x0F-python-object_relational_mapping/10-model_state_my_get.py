#!/usr/bin/python3

"""
A script that prints the State object
with the name passed as argument
from the database hbtn_0e_6_usa
"""

# Import needed modules & methods
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

# Importing the script
if __name__ == '__main__':
    # Create engine
    if __name__ == '__main__':
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]),
                            pool_pre_ping=True)

    # Stablishing session
    Session = sessionmaker(bind=engine)

    # Create table by metadata
    Base.metadata.create_all(engine)

    # create session
    session = Session()

    # extract first state
    states = session.query(State) \
                .filter(State.name == argv[4]).one_or_none()

    # print state.id
    if states is None:
        print("Not found")
    else:
        print(states.id)

    session.close()
