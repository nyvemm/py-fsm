import unittest
from unittest import mock
from controllers.transition_controller import TransitionController


class TestTransitions(unittest.TestCase):
    def setUp(self):
        self.transition_controller = TransitionController()
        self.transition_name = 'Test Transition'
        self.from_state = 'Test State'
        self.to_state = 'Test State2'

    @mock.patch('controllers.transition_controller.TransitionController.add_transition')
    def test_post(self, mock_add_transition):
        mock_add_transition.return_value = {
            'transition_name': self.transition_name}
        result = self.transition_controller.add_transition(
            self.transition_name, self.from_state, self.to_state)
        mock_add_transition.assert_called_once_with(
            self.transition_name, self.from_state, self.to_state)
        self.assertEqual(result, {'transition_name': self.transition_name})

    @mock.patch('controllers.transition_controller.TransitionController.get_transitions')
    def test_get(self, mock_get_transitions):
        mock_get_transitions.return_value = [
            {'transition_name': self.transition_name}]
        result = self.transition_controller.get_transitions()
        mock_get_transitions.assert_called_once()
        self.assertEqual(result, [{'transition_name': self.transition_name}])

    @mock.patch('controllers.transition_controller.TransitionController.get_next_transition')
    def test_get_next_transition(self, mock_get_next_transition):
        mock_get_next_transition.return_value = {
            'transition_name': self.transition_name}
        result = self.transition_controller.get_next_transition(
            self.transition_name)
        mock_get_next_transition.assert_called_once_with(self.transition_name)
        self.assertEqual(result, {'transition_name': self.transition_name})


if __name__ == '__main__':
    unittest.main()
