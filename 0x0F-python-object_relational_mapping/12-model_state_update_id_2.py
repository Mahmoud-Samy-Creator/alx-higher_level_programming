#!/usr/bin/python3

"""
a script that changes
the name of a State object from the database
"""

# Import important modules & methods
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    # Establish & create a session
    # Retrive & modify data
    Session = sessionmaker(bind=engine)
    Base.metadata.creat_all(engine)
    session = Session()

    # Query & commit
    renamed = session.query(State) \
                     .filter(State.id == 2).first()
    renamed.name = 'New Mexico'
    session.commit()

    # clean
    session.stop()
