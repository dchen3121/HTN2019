from typing import Dict
import uuid
from dataclasses import dataclass, field

from models.model import Model
from common.utils import Utils
import models.user.errors as errors

from firebase_admin import auth #TODO: may move this functionality elsewhere
# to initialize the app: default_app = firebase_admin.initialize_app()

@dataclass(eq=False)
class User(Model):

    collection: str = field(init=False, default='users')
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls.find_one_by('email', email)
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
            User(email, Utils.hash_password(password)).save_to_mongo()
        return True

    @classmethod
    def is_login_valid(cls, email: str, password: str) -> bool:
        user = cls.find_by_email(email)
        if not Utils.check_hashed_password(password, user.password):
            raise errors.IncorrectPasswordError('The password entered was incorrect.')
        return True

    @classmethod
    def update_slouch_data():
    #TODO: send slouch notif command to FCM
    # using the firebase admin sdk for python
    # specs: https://firebase.google.com/docs/reference/admin/python/firebase_admin.messaging#webpushnotification
    firebase_admin.messaging.WebpushNotification("Look out, you're slouching!", None, "ICON_URL")

    #update times slouched list
    #TODO: does mongo have same specifics (or can we just update and it'll create regardless?)
    #TODO: remove the users.val(); still want to find+update data
    if users.val() == None:
        #SET initial data value for user
        data = {'timesSlouched': [  #TODO: decide how we actually want to store data???
                {'date' : Utils.get_date(), 'numSlouch' : 0},
                {'date' : Utils.get_date(), 'numSlouch' : 0},
                {'date' : Utils.get_date(), 'numSlouch' : 0},
                {'date' : Utils.get_date(), 'numSlouch' : 0},
                {'date' : Utils.get_date(), 'numSlouch' : 0},
                {'date' : Utils.get_date(), 'numSlouch' : 0},
                {'date' : Utils.get_date(), 'numSlouch' : 1}]}
        #TODO: set data
    else:
        #UPDATE data value
        data = users.val()
        if data[6]['numSlouch'] != Utils.get_date():
            #add new day to list
            for i in range(0, 5):
                data[i] = data[i+1]
            data[6] = {'date' : Utils.get_date(), 'numSlouch' : 1}
        else:
            data[6]['numSlouch'] = data[6]['numSlouch'] + 1
        #TODO: update data

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
