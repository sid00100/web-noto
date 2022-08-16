from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, length, EqualTo


class Signup(FlaskForm):
    username = StringField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(
        validators=[DataRequired(),  length(min=8, max=22)])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(validators=[DataRequired()])


class Login(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])