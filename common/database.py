from typing import Dict
import pyrebase
import os


class Database:
    # For localhost testing
    # URI = "mongodb://127.0.0.1:27017/pricing"
    # DATABASE = pymongo.MongoClient(URI).get_database()

    config = {
        "apiKey": "apiKey",
        "authDomain": "htn2019-d987b.firebaseapp.com",
        "databaseURL": "https://htn2019-d987b.firebaseio.com",
        "storageBucket": "htn2019-d987b.appspot.com",
        # "serviceAccount": "path/to/serviceAccountCredentials.json"
    }

    URI = os.environ.get('MONGODB_URI')
    DATABASE = pyrebase.initialize_app(config)
    AUTH = DATABASE.auth()

    @staticmethod
    def insert(username: str, data: Dict):
        Database.DATABASE.child('users').child(username).set(data)

    @staticmethod
    def find(username: str, query: Dict):
        return Database.DATABASE.child('users').child(username).child(query).get().val()

    @staticmethod
    def find_one(username: str, query: Dict) -> Dict:   #TODO: this may not be necessary?
        return Database.DATABASE.child('users').child(username).child(query).get().val()

    @staticmethod
    def update(username: str, data: Dict):
        Database.DATABASE.child('users').child(username).update(data)

    @staticmethod
    def remove(username: str, query: Dict):
        Database.DATABASE.child('users').child(username).child(query).remove()

    #TODO: update if needed or delete
    @staticmethod
    def find_all_sorted_by(username: str, query: Dict, key: str, ascending: bool):
        if ascending:
            return Database.DATABASE.child('users').child(username).find(query).sort(key, pymongo.ASCENDING)
        return Database.DATABASE.child('users').child(username).find(query).sort(key, pymongo.DESCENDING)

    @staticmethod
    def new_user(email: str, password: str):
        auth.create_user_with_email_and_password(email, password)
