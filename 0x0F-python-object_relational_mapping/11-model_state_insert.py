#!/usr/bin/python3

"""
Title: Add a new state
Description: Script that adds the State object “Louisiana” to the database
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
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    # seen = False
    new_obj = State(name='Louisiana')
    session.add(new_obj)
    obj = session.query(State).filter_by(name='Louisiana').first()
    print(obj.id)
    session.commit()

    session.close()
