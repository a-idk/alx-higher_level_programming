#!/usr/bin/python3

"""
Title: From city
Description: Script dat lists all City objects 4m the database hbtn_0e_101_usa
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
        for city in state_obj.cities:
            # following the format (1: San Francisco -> California)
            print(city.id, city.name, sep=": ", end="")
            print(" -> " + state_obj.name)


    session.close()
