#!/usr/bin/python3
"""
Title: All states via SQLAlchemy
Description: Script that lists all State objects from the database
    hbtn_0e_6_usa
Author: @a_idk scripting
"""

from model_state import State, Base
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

    for obj in session.query(State).order_by(State.id):
        print("{}: {}".format(obj.id, obj.name))

    session.close()
