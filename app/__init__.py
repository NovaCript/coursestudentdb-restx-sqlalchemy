from flask import Flask
from .extentions import api, db
from .resources import ns


def create_app():
    app: Flask = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    with app.app_context():
        db.drop_all()
        db.create_all()

    return app
