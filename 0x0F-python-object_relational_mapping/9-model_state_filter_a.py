#!/usr/bin/python3

"""
script that lists all State objects
that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

# Importing needed module & methods
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Running the script
if __name__ == "__main__":
    # creating engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]))

    # Establishing session
    Session = sessionmaker(bind=engine)

    # Create the table
    Base.metadata.create_all(engine)

    # Make session
    session = Session()

    # Extract states containing letter 'a'
    states = session.query(State).filter(State.name.ilike('%a%')) \
                    .order_by(State.id).all()

    # Print state
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    # Closing the session
    session.close()
