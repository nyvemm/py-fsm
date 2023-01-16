
import unittest
from models.db import db
from flask_sqlalchemy import SQLAlchemy


class SQLAlchemyTest(unittest.TestCase):
    def test_db_instance(self):
        self.assertIsInstance(db, SQLAlchemy)


if __name__ == '__main__':
    unittest.main()
