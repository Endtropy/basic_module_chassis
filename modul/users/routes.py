from flask import Blueprint, jsonify, abort, g
from flask_restful import Resource, Api, reqparse

from modul import auth, db
from modul.models import User

users = Blueprint('users', __name__)
users_api = Api(users)

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='User name', location='json')
parser.add_argument('email', type=str, help='User email', location='json')
parser.add_argument('password', type=str, help='password', location='json')


class Users(Resource):
    """
    User Endpoint
    get  - basic authentication
    post - new user registration
    delete - delete user
    """

    @auth.login_required
    def get(self):
        """
        Basic login
        ---
        tags:
          - Users
        produces:
          - application/json
        security:
          - BasicAuth: []
        securityDefinitions:
          BasicAuth:
            type: basic
        responses:
          '200':
            description: User logged in
          '401':
            description: Unauthorized
        """

        return jsonify(f'User {g.user.username} logged in')

    @auth.login_required
    def post(self):
        """
        Register new user
        ---
        tags:
          - Users
        produces:
          - application/json
        parameters:
          - in: body
            description: Create new user
            name: user
            type: object
            properties:
              username:
                type: string
              password:
                type: string
              email:
                type: string
        schema:
            type: object
            properties:
              userName:
                type: string
              firstName:
                type: string
              lastName:
                type: string
        security:
          - BasicAuth: []
        securityDefinitions:
          BasicAuth:
            type: basic
        responses:
          '201':
            description: User is successfully registered
          '400':
            description: Registered is unsuccessful because of invalid input
        """
        username = parser.parse_args()['username']
        email = parser.parse_args()['email']
        password = parser.parse_args()['password']
        if username is None or password is None or email is None:
            abort(400, {'message': 'Username,password or email is missing'})  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400, {'message': 'Username is used'})  # existing user
        if User.query.filter_by(email=email).first() is not None:
            abort(400, {'message': 'Email address is used'})  # existing user
        user = User(username=username, email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'username': user.username}), 201

    @auth.login_required
    def delete(self):
        """
        Delete new user
        ---
        tags:
          - Users
        produces:
          - application/json
        parameters:
          - in: body
            description: User name
            name: username
            type: string
            required: true
            schema:
              type: string
              items:
                username : username
        security:
          - BasicAuth: []
        securityDefinitions:
          BasicAuth:
            type: basic
        responses:
          '200':
            description: User is successfully deleted
          '400':
            description: Registered is unsuccessful because of invalid input
        """
        username = parser.parse_args()['username']
        if User.query.filter_by(username=username).first() is None:
            abort(400, {'message': f'Username {username} not found'})  # existing user
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'{username} deleted'}), 200


users_api.add_resource(Users, '/user')


