
from controllers.state_controller import StateController
from flask import Flask
from models.db import db
from models.state_model import State
from models.transition_model import Transition
import os
import unittest


class TestStateController(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        app.app_context().push()
        self.state_controller = StateController()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_state_exists(self):
        state_name = 'test_state'
        state = State(name=state_name)
        db.session.add(state)
        db.session.commit()
        self.assertTrue(self.state_controller.state_exists(state_name))

    def test_add_state(self):
        state_name = 'test_state'
        new_state = self.state_controller.add_state(state_name)
        self.assertEqual(new_state['message'], 'State added successfully')
        self.assertEqual(new_state['state']['name'], state_name)
        existing_state = State.query.filter_by(name=state_name).first()
        self.assertIsNotNone(existing_state)

    def test_get_states(self):
        state_name = 'test_state'
        state = State(name=state_name)
        db.session.add(state)
        db.session.commit()
        states = self.state_controller.get_states()
        self.assertIn(state_name, states)


if __name__ == '__main__':
    unittest.main()
