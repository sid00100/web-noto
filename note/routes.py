from flask import render_template, request, redirect, url_for

from note import app, db_ref, db_ref_user
from note.signup import Signup, Login
from firebase_admin import auth

# import firebase_admin
# from firebase_admin import credentials


@app.route('/')
def index():
    return redirect(url_for("signup"))


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
                db_updater = {
                    "user": {
                        "username": username,
                        "email": email,
                        "notes":[
                            {
                            "title":"",
                            "description":"",
                            "time_of_creation":""
                        }
                        ]
                    }                    
                }
                user = auth.create_user(email=email, password=password)
                db_ref.push(db_updater)

            except Exception as e:
                print(e)

    return render_template('signup.html', form=signup)


@app.route('/login', methods=["GET", "POST"])
def login():
    login = Login()
    if request.method == "POST":
        email = login.email.data
        password = login.password.data
        try:
            login = auth.sign_in_with_email_and_password(email, password)
        except Exception as e:
            print(e)
    return render_template('login.html', login = login)
