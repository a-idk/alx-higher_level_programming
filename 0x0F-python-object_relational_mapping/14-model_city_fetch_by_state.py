#!/usr/bin/python3

"""
Title: Cities in state
Description: Script dat prints all City objects 4m the database hbtn_0e_14_usa
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

    session = sessionmaker(bind=engine)()

    state_city = session.query(State, City).join(City).order_by(City.id).all()
    for st, cty in state_city:
        print('{}: ({}) {}'.format(st.name, cty.id, cty.name))

    session.close()
