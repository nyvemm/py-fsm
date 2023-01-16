import os
import unittest
from unittest.mock import patch
from alembic import command


class AlembicTest(unittest.TestCase):
    @patch('os.environ.get')
    @patch('alembic.command.upgrade')
    def test_upgrade_head(self, mock_upgrade, mock_env_get):
        mock_env_get.return_value = 'database_url'
        from alembic.config import Config
        alembic_cfg = Config("alembic.ini")
        alembic_cfg.set_main_option(
            "sqlalchemy.url", os.environ.get("DATABASE_URL"))
        command.upgrade(alembic_cfg, "head")
        mock_upgrade.assert_called_with(alembic_cfg, "head")
        mock_env_get.assert_called_with('DATABASE_URL')


if __name__ == '__main__':
    unittest.main()
