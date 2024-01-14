#!/usr/bin/python3

"""
Title: Delete states
Description: Script that deletes all State objects with a name containing
    the letter a from the database hbtn_0e_6_usa
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

    for state_obj in session.query(State):
        if "a" in state_obj.name:
            session.delete(state_obj)
    session.commit()  # save changes

    session.close()
