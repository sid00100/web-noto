from note import psql_db

from flask_login import UserMixin


class Notes(psql_db.Model):
    id = psql_db.Column(psql_db.Integer, primary_key=True)
    user_id = psql_db.Column(psql_db.Integer, psql_db.ForeignKey("user.id"))
    title = psql_db.Column(psql_db.String(50), nullable=False)
    description = psql_db.Column(psql_db.Text, nullable=False)
    create_date = psql_db.Column(psql_db.DateTime, nullable=False)

    def __init__(self, user_key, title, description, create_date):
        self.user_key = user_key
        self.title = title
        self.description = description
        self.create_date = create_date


class User(psql_db.Model, UserMixin):
    id = psql_db.Column(psql_db.Integer, primary_key=True)
    username = psql_db.Column(psql_db.String(80), unique=True, nullable=False)
    email = psql_db.Column(psql_db.String(120), unique=True, nullable=False)
    pass_hash = psql_db.Column(psql_db.String(
        200), unique=True, nullable=False)
    notes_relation = psql_db.relationship("Notes", backref="noter")

    def __init__(self, username, email, pass_hash):
        self.username = username,
        self.email = email,
        self.pass_hash = pass_hash
