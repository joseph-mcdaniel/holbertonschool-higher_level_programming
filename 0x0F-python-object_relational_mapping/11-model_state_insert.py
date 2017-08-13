#!/usr/bin/python3
"""
adds the State object "Louisiana"
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()
    print(new_state.id)
