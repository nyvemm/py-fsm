from models.db import db
from models.state_model import State


class StateController:
    def add_state(self, state_name):
        existing_state = State.query.filter_by(name=state_name).first()
        if existing_state:
            raise ValueError('State already exists')
        new_state = State(name=state_name)
        db.session.add(new_state)
        db.session.commit()
        return {'message': 'State added successfully', 'state': new_state.as_dict()}

    def get_states(self):
        states = State.query.all()
        return {'states': [{**state.as_dict(), 'transitions': [transition.as_dict() for transition in state.transitions]} for state in states]}
