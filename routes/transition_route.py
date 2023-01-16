from flask import request
from flask_restx import Resource, Namespace, fields
from helpers.json_response import json_response
from controllers.transition_controller import TransitionController

transition_bp = Namespace(
    'Transitions', description='Create and list transitions', path='/')
transition_controller = TransitionController()


@transition_bp.route('/transitions')
class Transitions(Resource):
    @transition_bp.expect(transition_bp.model('Transition', {
        'transition_name': fields.String(required=True, description='The name of the transition'),
        'from_state': fields.String(required=True, description='The state to transition from'),
        'to_state': fields.String(required=True, description='The state to transition to')
    }))
    @json_response
    def post(self):
        """ Add a transition """
        if 'transition_name' not in request.json or 'from_state' not in request.json or 'to_state' not in request.json:
            raise ValueError(
                'Transition name, from state, and to state are required')
        transition_name = request.json['transition_name']
        from_state = request.json['from_state']
        to_state = request.json['to_state']
        return transition_controller.add_transition(transition_name, from_state, to_state)

    @json_response
    def get(self):
        """ Get all transitions """
        return transition_controller.get_transitions()


@transition_bp.route('/next/<current_transition>')
class NextTransition(Resource):
    @json_response
    def get(self, current_transition):
        """ Get the next transition associated with the current transition """
        return transition_controller.get_next_transition(current_transition)
