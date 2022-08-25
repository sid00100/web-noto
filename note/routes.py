from flask import render_template, request, redirect, url_for, session, json
import bcrypt
import bson
import requests
from note import app, user_collection, notes_collection, bcrypt_app
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
        password_hash = bcrypt_app.generate_password_hash(
            password).decode("utf-8")
        email = signup.email.data
        insert_login = {
            "email": email,
            "username": username,
            "password": password_hash
        }
        print(username, password, email)
        if signup.validate_on_submit:
            try:
                if user_collection.find_one({
                    "email": email,
                    "username": username
                }, {"_id": 0, "password": 0}) == {"email": email, "username": username}:
                    print("hola mf")
                    return render_template("signup.html", form=signup)
                else:
                    user_collection.insert_one(insert_login)
                    return render_template("login.html")
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
            email = login.email.data
            password = login.password.data
            login_data = user_collection.find_one({"email": email})
            pw_hash = login_data["password"]
            if bcrypt_app.check_password_hash(pw_hash, password):
                session_var = login_data["_id"]
                return render_template("index.html")
        except Exception as e:
            print("password did not match")

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


@app.route("/create-note", methods=["GET", "POST"])
def create():
    # bson_local_id = session["local_id"].bson
    bson_local_id = bson.ObjectId(session["local_id"])
    my_query = {"firebase_auth_id": bson_local_id}
    update = request.get_json(force=True)
    print(update)
    print(notes_collection)
    create_note = {"$set": {
        "title": update["title"],
        "description": update["description"],
        "date": update["date"]
    }}
    print("note-created")
    print(create_note)
    notes_collection.update_one(my_query, create_note)
    return "note-created"
# date, title, description
