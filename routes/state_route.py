from flask import Blueprint, request
from helpers.json_response import json_response
from controllers.state_controller import StateController

state_bp = Blueprint('state', __name__)
state_controller = StateController()


@state_bp.route('/add_state', methods=['POST'])
@json_response
def add_state():
    if 'state_name' not in request.json:
        raise ValueError('State name is required')

    state_name = request.json['state_name']
    return state_controller.add_state(state_name)

@state_bp.route('/get_states', methods=['GET'])
@json_response
def get_states():
    return state_controller.get_states()
