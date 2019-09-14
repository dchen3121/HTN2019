from typing import Dict
import pyrebase
import os
from urllib.parse import quote
import firebase_admin
from firebase_admin import credentials


class Database:
    # For localhost testing
    # URI = "mongodb://127.0.0.1:27017/pricing"
    # DATABASE = pymongo.MongoClient(URI).get_database()

    config = {
        "apiKey": "AIzaSyBSO7IT5_sfrmwWq-qUH8iBskqq5N7A_08",
        "authDomain": "htn2019-d987b.firebaseapp.com",
        "databaseURL": "https://htn2019-d987b.firebaseio.com",
        "storageBucket": "htn2019-d987b.appspot.com",
        "serviceAccount": "do_not_commit/htn2019-d987b-firebase-adminsdk-pz1d6-52193b1ef8.json"
    }

    firebase = pyrebase.initialize_app(config)
    DATABASE = firebase.database()
    AUTH = firebase.auth()

    @staticmethod
    def insert(username: str, data: Dict):
        Database.DATABASE.child('users').child(username.split('@')[0]).set(data)

    @staticmethod
    def find(username: str):
        return Database.DATABASE.child('users').child(username.split('@')[0]).get()

    @staticmethod
    def find_one(username: str, field: str) -> Dict:
        return Database.DATABASE.child('users').child(username.split('@')[0]).get().val().get(field)

    @staticmethod
    def update(username: str, data: Dict):
        Database.DATABASE.child('users').child(username.split('@')[0]).update(data)

    @staticmethod
    def remove(username: str, query: Dict):
        Database.DATABASE.child('users').child(username.split('@')[0]).child(query).remove()

    @staticmethod
    def new_user(user):
        Database.AUTH.create_user_with_email_and_password(email, password)
        Database.DATABASE.child('users').set(user.email.split('@')[0])
        Database.DATABASE.child('users').child(email.split('@')[0]).set(user.json())
