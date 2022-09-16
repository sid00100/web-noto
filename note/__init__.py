# import flask
from flask import Flask

# import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# import flask-login
from flask_login import LoginManager

# flask setup
app = Flask(__name__)

# sqlalchemy setup
psql_db = SQLAlchemy(app)

# sql alchemy database uri setup
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://webn:sid00100@localhost:5432/webn"

# flask secret key setup
app.config["SECRET_KEY"] = "SECRET"

# importing user (must stay here not above)
from note.db import Notes

# creating the login manager object
login_manager = LoginManager(app)

# setting up of login view
login_manager.login_view = "routes.login"

# setting up of user loader
from note.db import User
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))