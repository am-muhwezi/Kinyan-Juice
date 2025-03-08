from flask import Flask
from .utils import db
from .config.config import config_dict
from .auth.views import auth_namespace
from .models.users_db_model import User
from flask_restx import Api
from flask_jwt_extended import JWTManager

def create_app(config=config.Config_dict['prod']):
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    api = Api(app)

    jwt = JWTManager(app)

    api.add_namespace(auth_namespace, path='/auth')



    return app