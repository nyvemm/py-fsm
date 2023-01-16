import unittest
from models.db import db
from flask import jsonify
from helpers.logger import logger
from unittest.mock import MagicMock, patch
from helpers.json_response import json_response


class TestJsonResponse(unittest.TestCase):
    @patch('helpers.logger.logger.error')
    @patch('models.db.db.session.rollback')
    def test_json_response_exception(self, mock_rollback, mock_logger_error):
        @json_response
        def test_func():
            raise Exception('test exception')

        response, code = test_func()

        self.assertEqual(response, {'message': 'test exception'})
        self.assertEqual(code, 500)
        mock_rollback.assert_called_once()
        mock_logger_error.assert_called_once()

    @patch('helpers.logger.logger.error')
    @patch('models.db.db.session.rollback')
    def test_json_response_success(self, mock_rollback, mock_logger_error):
        @json_response
        def test_func():
            return {'message': 'test success'}

        response = test_func()

        self.assertEqual(response, {'message': 'test success'})
        mock_rollback.assert_not_called()
        mock_logger_error.assert_not_called()


if __name__ == '__main__':
    unittest.main()
