from flask import request
from helpers.json_response import json_response
from flask_restx import Resource, Namespace, fields
from controllers.state_controller import StateController


state_bp = Namespace(
    'States', description='Create and list states', path='/')
state_controller = StateController()


@state_bp.route('/states')
class States(Resource):
    @state_bp.expect(state_bp.model('State', {
        'state_name': fields.String(required=True, description='The name of state')
    }))
    @json_response
    def post(self):
        """ Add a state """
        if 'state_name' not in request.json:
            raise ValueError('State name is required')

        state_name = request.json['state_name']
        return state_controller.add_state(state_name)

    @json_response
    def get(self):
        """ Get all states """
        return state_controller.get_states()
