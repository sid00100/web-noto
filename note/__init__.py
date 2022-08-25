from flask import Flask
from flask_bcrypt import Bcrypt

from pymongo import MongoClient
# developement test code
# id - root
# pass - uyXTM2DiXx7DrMGy


app = Flask(__name__)
bcrypt_app = Bcrypt(app)

app.config["SECRET_KEY"] = "SECRET"


dbclient = MongoClient(
    "mongodb+srv://root:uyXTM2DiXx7DrMGy@web-noto-cluster.y31dhww.mongodb.net/?retryWrites=true&w=majority")
db = dbclient["web-noto"]
user_collection = db["users"]
notes_collection = db["notes"]
