#!/usr/bin/python3

"""
a script that adds
the State object “Louisiana” to the
database hbtn_0e_6_usa
"""

# Import needed modules
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Running script
if __name__ == "__main__":

    # Create new object --> new record
    Louisiana = State(name='Louisiana')

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    # Establish session
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Add created object and commit
    session.add(Louisiana)
    session.commit()

    # print state.id
    state = session.query(State).filter(State.name == 'Louisiana').one()
    print(state.id)

    # closing the session
    session.close()
