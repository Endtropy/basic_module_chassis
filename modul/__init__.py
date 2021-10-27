from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flasgger import Swagger

from modul.config import config

db = SQLAlchemy()
bcrypt = Bcrypt()
auth = HTTPBasicAuth()



def create_app():
    app = Flask(__name__)

    # blueprints
    from modul.api.routes import api
    from modul.users.routes import users
    app.register_blueprint(api)
    app.register_blueprint(users)

    # swagger
    Swagger(app, template=config.SWAGGER)

    # db
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # bcrypt
    bcrypt.init_app(app)

    return app