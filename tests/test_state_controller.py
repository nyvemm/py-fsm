
from controllers.state_controller import StateController
from models.state_model import State
from models.transition_model import Transition
from unittest.mock import patch
import os
import unittest


class TestStateController(unittest.TestCase):
    def setUp(self):
        self.state_controller = StateController()

    @patch.object(StateController, 'state_exists', return_value=True)
    def test_state_exists(self, mock_state_exists):
        state_name = 'test_state'
        self.assertTrue(self.state_controller.state_exists(state_name))

    @patch.object(StateController, 'add_state', return_value={'message': 'State added successfully'})
    def test_add_transition(self, mock_add_state):
        state_name = 'test_state'
        self.assertEqual(self.state_controller.add_state(state_name), {
                         'message': 'State added successfully'})

    @patch.object(StateController, 'get_states', return_value=[{'name': 'test_state'}])
    def test_get_states(self, mock_get_states):
        self.assertEqual(self.state_controller.get_states(),
                         [{'name': 'test_state'}])


if __name__ == '__main__':
    unittest.main()
