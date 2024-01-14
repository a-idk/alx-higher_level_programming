#!/usr/bin/python3

"""
Title: Contains `a`
Description: Script that lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
Author: @a_idk scripting
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )

    session = sessionmaker(bind=engine)()

    """
    obj = session.query(State).filter(State.name.contains('a')).order_by(
        State.id).all()
    for state in obj:
        print('{}: {}'.format(state.id, state.name))
    """
    for obj in session.query(State).order_by(State.id):
        if "a" in obj.name:
            print("{}: {}".format(obj.id, obj.name))

    session.close()
