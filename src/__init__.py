import os
from flask import Flask
from src.auth import auth
from src.database import db, ma


def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:

        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

    else:
        app.config.from_mapping(test_config)
    
    db.app = app
    db.init_app(app)

    ma.app = app
    ma.init_app(app)

    app.register_blueprint(auth)
    return app