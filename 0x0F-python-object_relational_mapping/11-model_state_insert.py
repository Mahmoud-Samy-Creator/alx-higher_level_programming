#!usr/bin/python3

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

    # Create data
    Base.metadata.create(engine)

    # Create session
    session = Session()

    # Add created object
    session.add(Louisiana)

    # print all data
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.name, state.id))
