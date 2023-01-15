from flask import Flask
from models.db import db
from scripts.config import Config
from flask_restx import Api


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    api = Api(app, title='Finite state machine',
              version='1.0', description='A finite state machine is a mathematical model that describes a system that can be in one of a finite number of states. The system can change from one state to another in response to an event. The event can be a user action, a received message, a time condition, etc. The system can change from one state to another in response to an event. The event can be a user action, an incoming message, a time condition, etc.')

    from routes.state_route import state_bp
    from routes.transition_route import transition_bp
    api.add_namespace(state_bp)
    api.add_namespace(transition_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
