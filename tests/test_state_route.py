import unittest
from unittest import mock
from controllers.state_controller import StateController


class TestStates(unittest.TestCase):
    def setUp(self):
        self.state_controller = StateController()
        self.state_name = 'New York'

    @mock.patch('controllers.state_controller.StateController.add_state')
    def test_post(self, mock_add_state):
        mock_add_state.return_value = {'state_name': self.state_name}
        result = self.state_controller.add_state(self.state_name)
        mock_add_state.assert_called_once_with(self.state_name)
        self.assertEqual(result, {'state_name': self.state_name})

    @mock.patch('controllers.state_controller.StateController.get_states')
    def test_get(self, mock_get_states):
        mock_get_states.return_value = [{'state_name': self.state_name}]
        result = self.state_controller.get_states()
        mock_get_states.assert_called_once()
        self.assertEqual(result, [{'state_name': self.state_name}])

    @mock.patch('controllers.state_controller.StateController.get_transitions_from_state')
    def test_get_transitions_from_state(self, mock_get_transitions_from_state):
        mock_get_transitions_from_state.return_value = [
            {'state_name': self.state_name}]
        result = self.state_controller.get_transitions_from_state(
            self.state_name)
        mock_get_transitions_from_state.assert_called_once_with(
            self.state_name)
        self.assertEqual(result, [{'state_name': self.state_name}])


if __name__ == '__main__':
    unittest.main()
