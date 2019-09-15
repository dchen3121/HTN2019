from typing import Dict
import uuid

from models.model import Model
from common.utils import Utils
from models.user import errors as errors
from common.database import Database

import firebase_admin
from firebase_admin import auth, messaging 
messaging_app = firebase_admin.initialize_app()


class User(Model):

    def __init__(self, email: str, password: str, 
                 data: Dict = {'timesSlouched': [
                                {'date': "2019-09-09", 'numSlouch': 7},
                                {'date': "2019-09-10", 'numSlouch': 13},
                                {'date': "2019-09-11", 'numSlouch': 15},
                                {'date': "2019-09-12", 'numSlouch': 10},
                                {'date': "2019-09-13", 'numSlouch': 7},
                                {'date': "2019-09-14", 'numSlouch': 11},
                                {'date': "2019-09-15", 'numSlouch': 0}
                            ]}):
        self.collection = 'users'
        self.email = email
        self.password = password
        self.data = data

    @classmethod
    def find_by_email(cls, email: str):
        try:
            return Database.find(email)
        except TypeError:
            # user not found by email
            raise errors.UserNotFoundError('A user with this email was not found.')

    @classmethod
    def register_user(cls, email: str, password: str):
        if not Utils.email_is_valid(email):
            # email is invalid
            raise errors.InvalidEmailError('The email does not have the right format.')
        # try:
        #     cls.find_by_email(email)  # this just checks it
        #     # email already exists
        #     raise errors.UserAlreadyExistsError('The email you used to register already exists.')
        # except errors.UserNotFoundError:
        #     # success!
        # try:
        Database.insert(email, {
                'password': Utils.hash_password(password),
                'timesSlouched': [
                    {'date': "2019-09-09", 'numSlouch': 7},
                    {'date': "2019-09-10", 'numSlouch': 13},
                    {'date': "2019-09-11", 'numSlouch': 15},
                    {'date': "2019-09-12", 'numSlouch': 10},
                    {'date': "2019-09-13", 'numSlouch': 7},
                    {'date': "2019-09-14", 'numSlouch': 11},
                    {'date': "2019-09-15", 'numSlouch': 0}
                ]
        })
        # except Exception as e:
        #     print(str(e))
        #     pass

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        # user = cls.find_by_email(email)
        # if not Utils.check_hashed_password(password, user.val()['password']): #XXX: not sure what object user will be
        #     raise errors.IncorrectPasswordError('The password entered was incorrect.')
        return True

    def update_slouch_data(self, email: str):
        # update times slouched list
        if not self.data:
            # SET initial data value for user
            self.data = {'timesSlouched': [
                            {'date': "2019-09-09", 'numSlouch': 7},
                            {'date': "2019-09-10", 'numSlouch': 13},
                            {'date': "2019-09-11", 'numSlouch': 15},
                            {'date': "2019-09-12", 'numSlouch': 10},
                            {'date': "2019-09-13", 'numSlouch': 7},
                            {'date': "2019-09-14", 'numSlouch': 11},
                            {'date': "2019-09-15", 'numSlouch': 0}
                        ]}
            self.data['timesSlouched'][6]['numSlouch'] += 1
            # self.add_to_firebase()
        else:
            #UPDATE data value
            if self.data['timesSlouched'][6]['date'] != Utils.get_date():
                #add new day to list
                for i in range(0, 5):
                    self.data[i] = self.data[i + 1]
                self.data['timesSlouched'][6] = {'date': Utils.get_date(), 'numSlouch': 1}
            else:
                self.data['timesSlouched'][6]['numSlouch'] += 1
            # self.add_to_firebase()
            self.save_to_firebase()

    @staticmethod
    def get_slouch_data(email: str) -> list:
        return Database.find_one(email, 'timesSlouched')
    
    def send_slouch_notif(self):
        # using the firebase admin sdk for python
        # specs: https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging#webpushnotification
        # This registration token comes from the client FCM SDKs.

        # See documentation on defining a message payload.
        message = messaging.Message(
            webpush=messaging.WebpushNotification(
                title="Look out, you're slouching!", 
                icon="ICON_URL"),
            to="/topics/all"
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send(message)
        # Response is a message ID string.

    def json(self) -> Dict:
        return {
            'password': self.password,
            'data': self.data
        }
