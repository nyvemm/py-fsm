from controllers.transition_controller import TransitionController
from flask import Flask
from models.db import db
from models.state_model import State
from models.transition_model import Transition
import os
import unittest


class TestTransitionController(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        app.app_context().push()
        self.transition_controller = TransitionController()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_transition(self):
        from_state_name = 'test_from_state'
        to_state_name = 'test_to_state'
        transition_name = 'test_transition'
        from_state = State(name=from_state_name)
        to_state = State(name=to_state_name)
        db.session.add(from_state)
        db.session.add(to_state)
        db.session.commit()
        new_transition = self.transition_controller.add_transition(
            transition_name, from_state_name, to_state_name)
        self.assertEqual(new_transition['message'],
                         'Transition added successfully')

    def test_get_transitions(self):
        from_state_name = 'test_from_state'
        to_state_name = 'test_to_state'
        transition_name = 'test_transition'
        from_state = State(name=from_state_name)
        to_state = State(name=to_state_name)
        transition = Transition(name=transition_name,
                                from_state=from_state_name, to_state=to_state_name)
        db.session.add(from_state)
        db.session.add(to_state)
        db.session.add(transition)
        db.session.commit()
        transitions = self.transition_controller.get_transitions()
        self.assertEqual(transitions[transition_name]['name'], transition_name)

    def test_decide_next_transition(self):
        from_state_name = 'test_from_state'
        to_state_name = 'test_to_state'
        transition_name = 'test_transition'
        from_state = State(name=from_state_name)
        to_state = State(name=to_state_name)
        transition = Transition(name=transition_name,
                                from_state=from_state_name, to_state=to_state_name)
        db.session.add(from_state)
        db.session.add(to_state)
        db.session.add(transition)
        db.session.commit()
        next_transition = self.transition_controller.decide_next_transition(transition, [
                                                                            transition])
        self.assertEqual(next_transition, transition)


if __name__ == '__main__':
    unittest.main()
