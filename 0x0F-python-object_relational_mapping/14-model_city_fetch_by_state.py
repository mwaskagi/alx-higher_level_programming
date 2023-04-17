#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    for state, city in session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(city.name, state.id, state.name))

    session.close()
