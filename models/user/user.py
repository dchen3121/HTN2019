from typing import Dict
import uuid

from models.model import Model
from common.utils import Utils
from models.user import errors as errors
from common.database import Database

import firebase_admin
from firebase_admin import auth #TODO: may move this functionality elsewhere
messaging_app = firebase_admin.initialize_app()


class User(Model):

    def __init__(self, email: str, password: str, 
                 data: Dict = {'timesSlouched': [
                                  {'date': Utils.get_date(), 'numSlouch': 0},
                                  {'date': Utils.get_date(), 'numSlouch': 0},
                                  {'date': Utils.get_date(), 'numSlouch': 0},
                                  {'date': Utils.get_date(), 'numSlouch': 0},
                                  {'date': Utils.get_date(), 'numSlouch': 0},
                                  {'date': Utils.get_date(), 'numSlouch': 0},
                                  {'date': Utils.get_date(), 'numSlouch': 0}
                              ]}):
        self.collection = 'users'
        self.email = email
        self.password = password
        self.data = data

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls(email=Database.find(email).key(), password=Database.find(email).val()['password'],
                       data=Database.find(email).val())
        except TypeError:
            # user not found by email
            raise errors.UserNotFoundError('A user with this email was not found.')

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            # email is invalid
            raise errors.InvalidEmailError('The email does not have the right format.')
        try:
            cls.find_by_email(email)  # this just checks it
            # email already exists
            raise errors.UserAlreadyExistsError('The email you used to register already exists.')
        except errors.UserNotFoundError:
            # success!
            User(email, Utils.hash_password(password)).register_model(email, Utils.hash_password(password))
        return True

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)
        if not Utils.check_hashed_password(password, user.data['password']): #XXX: not sure what object user will be
            raise errors.IncorrectPasswordError('The password entered was incorrect.')
        return True

    @classmethod
    def update_slouch_data(email: str):
        #update times slouched list
        user = cls.find_by_email(email)
        if not user:
            #SET initial data value for user
            data[6]['numSlouch'] = data[6]['numSlouch'] = data[6]['numSlouch'] + 1
            self.add_to_firebase()
        else:
            #UPDATE data value
            data = users.val()
            if data[6]['numSlouch'] != Utils.get_date():
                #add new day to list
                for i in range(0, 5):
                    date[i] = date[i + 1]
                data[6] = {'date': Utils.get_date(), 'numSlouch': 1}
            else:
                data[6]['numSlouch'] = data[6]['numSlouch'] + 1
            self.save_to_firebase()
    
    @classmethod
    def send_slouch_notif():
        # using the firebase admin sdk for python
        # specs: https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging#webpushnotification
        messaging_app.messaging.WebpushNotification("Look out, you're slouching!", None, "ICON_URL")

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
