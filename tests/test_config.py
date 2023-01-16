
from dotenv import load_dotenv
from scripts.config import Config
import os
import unittest


class TestConfig(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.config = Config()

    def test_env_variables_match(self):
        self.assertEqual(self.config.SQLALCHEMY_DATABASE_URI,
                         os.getenv("DATABASE_URL"))
        self.assertFalse(self.config.SQLALCHEMY_TRACK_MODIFICATIONS)


if __name__ == '__main__':
    unittest.main()
