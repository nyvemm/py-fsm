from models.state_model import State
from models.transition_model import Transition
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def seed_states(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(State).count() == 0:
        states = [
            State(name='acordado'),
            State(name='trabalhando'),
            State(name='descansando'),
            State(name='dormindo')
        ]
        session.add_all(states)
        session.commit()
    else:
        print("States table is not empty. Skipping seeding.")