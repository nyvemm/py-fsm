
from flask import Blueprint, request
from helpers.json_response import json_response
from controllers.transition_controller import TransitionController

transition_bp = Blueprint('transition', __name__)

transition_controller = TransitionController()


@transition_bp.route('/add_transition', methods=['POST'])
@json_response
def add_transition():
    if 'transition_name' not in request.json or 'from_state' not in request.json or 'to_state' not in request.json:
        raise ValueError(
            'Transition name, from state, and to state are required')
    transition_name = request.json['transition_name']
    from_state = request.json['from_state']
    to_state = request.json['to_state']

    return transition_controller.add_transition(transition_name, from_state, to_state)


@transition_bp.route('/get_transitions', methods=['GET'])
@json_response
def get_transitions():
    return transition_controller.get_transitions()
