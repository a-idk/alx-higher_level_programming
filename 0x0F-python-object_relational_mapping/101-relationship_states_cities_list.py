#!/usr/bin/python3

"""
Title: List relationship
Description: Script that lists all State objects, and corresponding City
    objects, contained in the database hbtn_0e_101_usa
Author: @a_idk scripting
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    for state_obj in session.query(State).order_by(State.id):
        print(state_obj.id, state_obj.name, sep=": ")
        for city in state_obj.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")


    session.close()
