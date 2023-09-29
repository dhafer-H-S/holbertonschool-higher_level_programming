#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.orm import Session
import model_state
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, database),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    the1state = session.query(State).first()
    if the1state is not None:
        print("{}: {}".format(the1state.id, the1state.name))
    else:
        print("Nothing")

    session.close()
