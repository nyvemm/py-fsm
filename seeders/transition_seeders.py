from models.transition_model import Transition
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def seed_transitions(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(Transition).count() == 0:
        transitions = [
            Transition(name='06:00', from_state='dormindo',
                       to_state='acordado', created_at='2023-01-01 06:00:00'),
            Transition(name='08:00', from_state='acordado',
                          to_state='trabalhando', created_at='2023-01-01 08:00:00'),
            Transition(name='12:00', from_state='trabalhando',
                       to_state='descansando', created_at='2023-01-01 12:00:00'),
            Transition(name='13:00', from_state='descansando',
                       to_state='trabalhando', created_at='2023-01-01 13:00:00'),
            Transition(name='18:00', from_state='trabalhando',
                       to_state='descansando', created_at='2023-01-01 18:00:00'),
            Transition(name='22:00', from_state='descansando',
                       to_state='dormindo', created_at='2023-01-01 22:00:00'),
        ]
        session.add_all(transitions)
        session.commit()
    else:
        print("Transitions table is not empty. Skipping seeding.")
