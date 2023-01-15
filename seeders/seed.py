from seeders.state_seeders import seed_states
from seeders.transition_seeders import seed_transitions


def seed(engine):
    seed_states(engine)
    seed_transitions(engine)
