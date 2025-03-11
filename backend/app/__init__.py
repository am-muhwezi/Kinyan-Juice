from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from .utils import db
from flask_cors import CORS
from .config.config import Config_dict
from .auth.views import auth_namespace
from .products.views import product_namespace
from .models.users_db_model import User
from .models.products import Product
from flask_migrate import Migrate



def create_app(config=Config_dict['dev']):

    app = Flask(__name__)

    CORS(app, supports_credentials=True)  
    app.config.from_object(config)
    db.init_app(app)
    api = Api(app)

    jwt = JWTManager(app)


    migrate = Migrate(app, db)
    api.add_namespace(auth_namespace, path='/auth')
    api.add_namespace(product_namespace, path='/products')


    @app.shell_context_processor
    def make_shell_context():
        return {
               'db': db,
               'User': User,
               'Products': Product
            }


    return app