
import unittest
import logging
from helpers.logger import logger


def generate_states():
    states = ['awake', 'sleeping', 'hungry']
    for state in states:
        yield state


class TestGenerateStates (unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def test_generate_states(self):
        states = ['awake', 'sleeping', 'hungry']
        for state in generate_states():
            self.assertIn(state, states)


if __name__ == '__main__':
    unittest.main()
