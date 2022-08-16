from flask import render_template, request, redirect, url_for, session
import requests

from note import app, db_ref, db_ref_user
from note.signup import Signup, Login
from firebase_admin import auth

# import firebase_admin
# from firebase_admin import credentials


@app.route('/')
def index():
    return render_template("index.html")
    # if session["local_id"] is not None:
    #     return render_template("index.html")
    # else:
    #     return redirect(url_for("signup"))


@app.route('/signup', methods=["GET", "POST"])
def signup():
    # bugs to be fixed here
    signup = Signup()
    if request.method == "POST":
        username = signup.username.data
        password = signup.password.data
        email = signup.email.data
        print(username, password, email)
        if signup.validate_on_submit:
            try:
                user = auth.create_user(email=email, password=password)

                login_req = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDctxasRoJa73pfr3rHYiP8NGpMLUDsMOM", json={
                    "email": email,
                    "password": password
                })
                user_uid = login_req.json()

                db_updater = {
                    "user": {
                        "firebase_auth_id": user_uid,
                        "username": username,
                        "email": email,
                        "notes": {}
                    }
                }
                db_ref.push(db_updater)

            except Exception as e:
                print(e)

    return render_template('signup.html', form=signup)


@app.route('/login', methods=["GET", "POST"])
def login():
    login = Login()
    if request.method == "POST":
        try:
            login_req = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDctxasRoJa73pfr3rHYiP8NGpMLUDsMOM", json={
                "email": login.email.data,
                "password": login.password.data
            })
            json_login_req_session = login_req.json()["localId"]
            session["local_id"] = json_login_req_session
            print(session)
        except Exception as e:
            print(e)
    return render_template('index.html', login=login)
    # return render_template(url_for("index"), login=login)
