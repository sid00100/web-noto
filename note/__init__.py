from flask import Flask

import firebase_admin
from firebase_admin import credentials
from pymongo import MongoClient
# developement test code
# id - root
# pass - uyXTM2DiXx7DrMGy


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"

cred = credentials.Certificate("note/note-app-db3be-firebase-adminsdk-zwm5y-f4d835d6d3.json")
firebase_admin.initialize_app(cred,{
    "databaseURL": "https://note-app-db3be-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

dbclient = MongoClient("mongodb+srv://root:uyXTM2DiXx7DrMGy@web-noto-cluster.y31dhww.mongodb.net/?retryWrites=true&w=majority")
db = dbclient["web-noto"]
user_collection = db["users"]