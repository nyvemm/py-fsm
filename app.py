from flask import Flask
from models.db import db
from scripts.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from routes.state_route import state_bp
    from routes.transition_route import transition_bp
    app.register_blueprint(state_bp)
    app.register_blueprint(transition_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()