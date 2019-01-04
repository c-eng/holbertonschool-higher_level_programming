#!/usr/bin/python3
"""list all State objects from hbtn_0e_6_usa which contain 'a'
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    states = session.query(State).all()
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
