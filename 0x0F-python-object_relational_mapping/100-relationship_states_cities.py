#!/usr/bin/python3

"""
Title: City relationship
Description: Script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
Author: @a_idk scripting
"""

from model_state import Base, State
from model_city import City
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

    session.add(City(name="San Francisco", state=State(name="California")))

    """state_obj = State(name="California")
    city_obj = City(name="San Francisco")

    state_obj.cities.append(city_obj)
    session.add(state_obj), session.add(city_obj)
    """
    session.commit()  # saves/persists changes

    session.close()
