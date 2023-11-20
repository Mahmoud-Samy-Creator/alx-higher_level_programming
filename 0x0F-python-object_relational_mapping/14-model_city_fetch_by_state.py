#!/usr/bin/python3

"""
A script that prints all City objects
from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    # extract all cities in a state
    cities = session.query(State, City) \
                    .filter(State.id == City.state_id)

    # print all states

    for ci in cities:
        print("{}: ({}) {}".format(ci.State.name, ci.City.id, ci.City.name))

    session.close()
