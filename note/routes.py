from flask import render_template, request, redirect, url_for, session
import requests
from note import app, psql_db
from note.signup import Signup, Login
from note.db import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required, current_user, logout_user


# index
@app.route('/')
@login_required
def index():
    return render_template("index.html", name = current_user.username)


# signup
@app.route('/signup', methods=["GET", "POST"])
def signup():
    signup = Signup()
    if request.method == "POST":
        username = signup.username.data
        password = signup.password.data
        hassed_password = generate_password_hash(password)
        email = signup.email.data
        print(username, password, email)
        if signup.validate_on_submit:
            try:
                user_data = User(username, email, hassed_password)
                psql_db.session.add(user_data)
                psql_db.session.commit()
                # may be u will like to add some random data to the database regarding to the current user
            except Exception as e:
                print(e)

    return render_template('signup.html', form=signup)


# login
@app.route('/login', methods=["GET", "POST"])
def login():
    login = Login()
    if request.method == "POST":
        try:
            logging_user_email = login.email.data
            logging_user_pass = login.password.data
            logging_user = User.query.filter_by(
                email=logging_user_email).first()
            if not logging_user and not check_password_hash(logging_user.password, logging_user_pass):
                print("invalid user credentials")
                return redirect(url_for("login"))
            else:
                print("successfully logged in")
                login_user(logging_user)
                return redirect(url_for("index"))
        except Exception as e:
            print(e)

    return render_template("login.html", login=login)


# logout
@app.route("/logout")
def logout():
    if session.get("local_id"):
        session.pop("local_id")
        return redirect(url_for("signup"))
    else:
        return redirect(url_for("signup"))


# edit
@app.route("/edit<note_id>")
def edit(note_id):
    pass

# create note
@login_required
@app.route("/create-note")
def create():
    logout_user()
# date, title, description
