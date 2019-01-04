#!/usr/bin/python3
""" print first state object from hbtn_0e_6_usa
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
    f_state = session.query(State).first()
    if f_state:
        print("{}: {}".format(f_state.id, f_state.name))
    else:
        print("Nothing")
