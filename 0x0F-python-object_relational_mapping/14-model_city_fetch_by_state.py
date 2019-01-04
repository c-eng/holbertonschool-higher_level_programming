#!/usr/bin/python3
""" Prints all city objects from passed database
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    cities = session.query(City).all()
    states = session.query(State).all()
    for city in cities:
        print("{}: ({}) {}".format(states[city.state_id - 1].name,
                                   city.id, city.name))
