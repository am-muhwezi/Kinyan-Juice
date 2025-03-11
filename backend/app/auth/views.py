from http import HTTPStatus
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from ..models.users_db_model import User 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
)
from werkzeug.exceptions import Conflict, BadRequest

auth_namespace = Namespace(
    'auth', description="namespace for all authentication")

signup_model = auth_namespace.model(
    'Signup', {
        'id': fields.Integer(),
        'fullname': fields.String(required=True, description="A Username"),
        'email': fields.String(required=True, description="An Email Address"),
        'password': fields.String(required=True,
                                       description="A Password"),
    }
)

user_model = auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'fullname': fields.String(required=True, description="A Username"),
        'email': fields.String(required=True, description="An Email Address"),
        'password': fields.String(required=True,
                                       description="A Password"),
        'is_staff': fields.Boolean(description="Shows User Is Staff"),
        'is_active': fields.Boolean(description="Shows User Active"),
    }
)

login_model = auth_namespace.model(
    'Login', {
        'email': fields.String(required=True, description="An Email Address"),
        'password': fields.String(required=True, description="A Password"),
    }
)


@auth_namespace.route('/signup')
class SignUp(Resource):

    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        """
        Create a new User account
        """
        data = request.get_json()

        
        new_user = User(
            fullname=data.get('fullname'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password')),
            )
        new_user.save()

        return new_user, HTTPStatus.CREATED

        
    


@auth_namespace.route('/login')
class Login(Resource):
    """
        Login Resource: Handles all login requests
    """

    @auth_namespace.expect(login_model)
    def post(self):
        """
        Generate JWT Pair
        """
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if (user is not None) and check_password_hash(user.password,
                                                      password):

            access_token = create_access_token(identity=user.fullname)

            response = {
                'access_token': access_token
            }

            return response, HTTPStatus.OK

        raise BadRequest("Invalid Username or Password")