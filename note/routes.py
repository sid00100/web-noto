from flask import render_template, request

from note import app
from note.signup import Signup
from firebase_admin import auth

# import firebase_admin
# from firebase_admin import credentials


@app.route('/')
def index():
    return render_template('index.html')


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
            except Exception as e:
                print(e)

    return render_template('signup.html', form=signup)


@app.route('/login')
def login():
    return render_template('login.html')
