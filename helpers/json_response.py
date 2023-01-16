from flask import jsonify
from functools import wraps
from helpers.logger import logger
from models.db import db

def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(e)
            db.session.rollback()
            return {'message': str(e)}, 500
    return wrapper