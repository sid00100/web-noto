from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, length


class Signup(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(
        validators=[DataRequired(),  length(min=8, max=22)])
    submit = SubmitField(validators=[DataRequired()])
