import random

from models.db import db
from models.state_model import State
from models.transition_model import Transition
from helpers.logger import logger


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

    def decide_next_transition(self, current_transition, possible_next_transitions):
        valid_transitions = [
            transition for transition in possible_next_transitions if transition.created_at > current_transition.created_at]

        logger.debug('Possible next transitions: {}'.format(
            possible_next_transitions))
        return valid_transitions[0] if valid_transitions else possible_next_transitions[0]

    def get_next_transition(self, current_transition):
        current_transition = Transition.query.filter_by(
            name=current_transition).first()
        if not current_transition:
            raise ValueError('Current transition does not exist')

        possible_next_transitions = Transition.query.filter_by(
            from_state=current_transition.to_state).all()
        if not possible_next_transitions:
            raise ValueError('There is no next transition')
        
        if len(possible_next_transitions) == 1:
            return possible_next_transitions[0].as_dict()
        
        else:
            next_transition = self.decide_next_transition(
                current_transition, possible_next_transitions)
            return next_transition.as_dict()
