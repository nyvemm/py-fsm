from models.db import db
from models.state_model import State
from models.transition_model import Transition


class TransitionController:
    def add_transition(self, transition_name, from_state, to_state):
        existing_transition = Transition.query.filter_by(
            name=transition_name).first()

        if existing_transition:
            raise ValueError('Transition already exists')

        from_state_exist = State.query.filter_by(name=from_state).first()
        if not from_state_exist:
            raise ValueError('From state does not exist')

        to_state_exist = State.query.filter_by(name=to_state).first()
        if not to_state_exist:
            raise ValueError('To state does not exist')

        new_transition = Transition(
            name=transition_name, from_state=from_state, to_state=to_state)
        db.session.add(new_transition)
        db.session.commit()
        return {'message': 'Transition added successfully', 'transition': new_transition.as_dict()}

    def get_transitions(self):
        transitions = Transition.query.all()
        return {t.name: t.as_dict() for t in transitions}
