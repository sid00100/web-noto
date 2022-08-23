from flask import render_template, request, redirect, url_for, session, json
import requests
from note import app, user_collection
from note.signup import Signup, Login
from firebase_admin import auth


# index
@app.route('/')
def index():
    if session.get("local_id") is not None:
        return render_template("index.html")
    else:
        return redirect(url_for("signup"))


# signup
@app.route('/signup', methods=["GET", "POST"])
def signup():
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
                user_uid = login_req.json().get("localId")

                db_updater = {
                    "firebase_auth_id": user_uid,
                    "username": username,
                    "email": email
                }

                user_collection.insert_one(db_updater)
            except Exception as e:
                print(e)

    return render_template('signup.html', form=signup)


# login
@app.route('/login', methods=["GET", "POST"])
def login():
    login = Login()
    print(session.get("local_id"))
    if request.method == "POST" and session.get("local_id") == None:
        try:
            login_req = requests.post("https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDctxasRoJa73pfr3rHYiP8NGpMLUDsMOM", json={
                "email": login.email.data,
                "password": login.password.data
            })

            session_var = login_req.json()["localId"]
            session["local_id"] = session_var

            return render_template("index.html")
        except Exception as e:
            print("error")

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
@app.route("/create-note")
def create():
    uid = session["local_id"]
# date, title, description
