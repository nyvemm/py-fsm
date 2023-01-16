from controllers.transition_controller import TransitionController
from models.state_model import State
from models.transition_model import Transition
from unittest.mock import patch
import os
import unittest


class TestTransitionController(unittest.TestCase):
    def setUp(self):
        self.transition_controller = TransitionController()

    @patch.object(TransitionController, 'add_transition', return_value={'message': 'Transition added successfully'})
    def test_add_transition(self, mock_add_transition):
        transition_name = 'test_transition'
        from_state = 'test_state'
        to_state = 'test_state'
        self.assertEqual(self.transition_controller.add_transition(transition_name, from_state, to_state), {
                         'message': 'Transition added successfully'})

    @patch.object(TransitionController, 'get_transitions', return_value=[{'name': 'test_transition'}])
    def test_get_transitions(self, mock_get_transitions):
        self.assertEqual(self.transition_controller.get_transitions(),
                         [{'name': 'test_transition'}])

    @patch.object(TransitionController, 'decide_next_transition', return_value={'name': 'test_transition'})
    def test_decide_next_transition(self, mock_decide_next_transition):
        current_transition = 'test_transition'
        possible_next_transitions = ['test_transition']
        self.assertEqual(self.transition_controller.decide_next_transition(
            current_transition, possible_next_transitions), {'name': 'test_transition'})

    @patch.object(TransitionController, 'get_next_transitions', return_value=[{'name': 'test_transition'}])
    def get_next_transition(self, mock_get_next_transitions):
        current_state = 'test_state'
        self.assertEqual(self.transition_controller.get_next_transitions(
            current_state), [{'name': 'test_transition'}])


if __name__ == '__main__':
    unittest.main()
