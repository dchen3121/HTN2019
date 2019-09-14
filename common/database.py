from typing import Dict
import pyrebase
import os


class Database:
    # For localhost testing
    # URI = "mongodb://127.0.0.1:27017/pricing"
    # DATABASE = pymongo.MongoClient(URI).get_database()

    config = {
        "apiKey": "apiKey",
        "authDomain": "projectId.firebaseapp.com",
        "databaseURL": "https://databaseName.firebaseio.com",
        "storageBucket": "projectId.appspot.com",
        "serviceAccount": "path/to/serviceAccountCredentials.json"
    }

    DATABASE = pyrebase.initialize_app(config)
    AUTH = firebase.auth()

    @staticmethod
    def insert(username: str, data: Dict):
        Database.DATABASE.child('users').child(username).set(data)

    @staticmethod
    def find(username: str):
        return Database.DATABASE.child('users').child(username).get().val()

    @staticmethod
    def find_one(username: str, query: Dict) -> Dict:
        return Database.DATABASE.child('users').child(username).child(query).get().val()

    @staticmethod
    def update(username: str, data: Dict):
        Database.DATABASE.child('users').child(username).update(data)

    @staticmethod
    def remove(username: str, query: Dict):
        Database.DATABASE.child('users').child(username).child(query).remove()

    @staticmethod
    def new_user(email: str, password: str):
        auth.create_user_with_email_and_password(email, password)
        Database.DATABASE.child('users').set(email)
        Database.DATABASE.child('users').child(email).set({'password': password})
