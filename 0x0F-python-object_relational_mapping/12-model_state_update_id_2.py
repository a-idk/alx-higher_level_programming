#!/usr/bin/python3

"""
Title: Update a state
Description: Script that changes the name of a State object from the database
    hbtn_0e_6_usa
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

    state_obj = session.query(State).filter_by(id=2).first()
    state_obj.name = "New Mexico"  # set state name to "New Mexico"
    session.commit()  # save changes

    session.close()
