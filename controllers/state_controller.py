from models.db import db
from models.state_model import State
from models.transition_model import Transition


class StateController:
    def state_exists(self, state_name):
        state = State.query.filter_by(name=state_name).first()
        return True if state else False

    def add_state(self, state_name):
        existing_state = self.state_exists(state_name)
        if existing_state:
            raise ValueError('State already exists')
        new_state = State(name=state_name)
        db.session.add(new_state)
        db.session.commit()
        return {'message': 'State added successfully', 'state': new_state.as_dict()}

    def get_states(self):
        states = State.query.all()
        return {state.name: {**state.as_dict('name'), 'transitions': {transition.name: transition.as_dict('name', 'from_state') for transition in state.transitions}} for state in states}

    def get_transitions_from_state(self, state_name):
        if not self.state_exists(state_name):
            raise ValueError('State does not exist')
        state_transitions = Transition.query.filter_by(
            from_state=state_name).all()
        return {transition.name: transition.as_dict('name', 'from_state') for transition in state_transitions}
