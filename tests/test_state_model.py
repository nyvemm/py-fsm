from datetime import datetime
from models.db import db
from models.state_model import State
from sqlalchemy import Column, String, ForeignKey
import unittest


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State(name='test', created_at=datetime.now())

    def test_as_dict(self):
        expected_dict = {
            'name': 'test',
            'created_at': self.state.created_at.isoformat()
        }
        self.assertDictEqual(self.state.as_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
