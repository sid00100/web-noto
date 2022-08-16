from flask import Flask, session

import firebase_admin
from firebase_admin import credentials, db




app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"

cred = credentials.Certificate("note/note-app-db3be-firebase-adminsdk-zwm5y-f4d835d6d3.json")
firebase_admin.initialize_app(cred,{
    "databaseURL": "https://note-app-db3be-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

db_ref = db.reference("/")
db_ref_user = db.reference("/-N9X6TBu9jO-N7_Ci-z5/user")