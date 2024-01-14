#!/usr/bin/python3

"""
Title: Get a state
Description: Script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa
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

    seen = False
    for obj in session.query(State):
        if obj.name == sys.argv[4]:
            print("{}".format(obj.id))
            seen = True
            break
    # check for not seen
    if seen is False:
        print("Not found")

    session.close()
