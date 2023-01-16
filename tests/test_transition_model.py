import unittest
from models.transition_model import Transition
from sqlalchemy import Column, String, ForeignKey


class TestTransition(unittest.TestCase):
    def setUp(self):
        self.transition = Transition(name="Test Transition",
                                     from_state="Test State", to_state="Test State2")

    def test_transition_as_dict(self):
        expected_dict = {
            'name': 'Test Transition',
            'created_at': None,
            'from_state': 'Test State',
            'to_state': 'Test State2'
        }
        self.assertDictEqual(self.transition.as_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
