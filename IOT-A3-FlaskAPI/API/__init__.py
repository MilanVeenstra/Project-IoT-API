from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
import os
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
basedir = os.path.abspath(os.path.dirname(__file__))
def create_api():
    app = Flask("DataAPI")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, DB_NAME)
    db.init_app(app)
    cors = CORS(app)
    api = Api(app)

    from API.routes.data_get import DataGet
    from API.routes.data_post import DataPost
    from API.routes.register_device import KeyRegister

    api.add_resource(DataGet, '/data/<command>')
    api.add_resource(DataPost, '/data/post')
    api.add_resource(KeyRegister, '/sign-up')

    from API.models.model_measurements import Measurements, Depth, Temperature
    from API.models.model_devices import Devices
    from API.models.model_logs import Logs

    create_database(app)

    return app


def create_database(app_name):
    if not path.exists('API/' + DB_NAME):
        with app_name.app_context():
            db.create_all()
            print('---- created database ----')
