#!/usr/bin/python3
"""" script that lists all State objects from the
database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
