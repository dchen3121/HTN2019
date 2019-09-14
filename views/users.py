from flask import request, session, render_template, Blueprint, redirect, url_for, flash
from models.user import User, errors, requires_login
from common.utils import Utils
import datetime

user_blueprint = Blueprint('users', __name__)

firebaseConfig = {  #TODO
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json" #optional; bypasses any security rules
}

firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the firebaseAuth service
firebaseAuth = firebase.firebaseAuth()
# Get a reference to the database service
firebaseDB = firebase.database()

user = None # user variable???

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # registering the user
        try:
            firebaseAuth.create_user_with_email_and_password(email, password)
            global user = firebasefirebaseAuth.sign_in_with_email_and_password(email, password)
            session['email'] = email

            # create a path to data per user in DB 
            firebaseDB.child("users").child.(email) 

            return redirect('/')
        except errors.UserError as e:
            flash(e.message, 'danger')
    return render_template('users/register.html')


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            # Log the user in
            global user = firebasefirebaseAuth.sign_in_with_email_and_password(email, password)
            return redirect('/')
            #TODO: every hour, need to run the following to get a new user token: user = firebasefirebaseAuth.refresh(user['refreshToken'])
        except errors.UserError as e:
            flash(e.message, 'danger')
    return render_template('users/login.html')


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect('/')

def user_slouch():
    #TODO: send slouch notif command to FCM

    #update times slouched list
    data = firebaseDB.child('users').child(user['email']).get() #TODO: uh does the email field even exist in user?
    if users.val() == None:
        #SET data value
        data = {'timesSlouched': [
                        {'date' : datetime.date, 'numSlouch' : 0},
                        {'date' : datetime.date, 'numSlouch' : 0},
                        {'date' : datetime.date, 'numSlouch' : 0},
                        {'date' : datetime.date, 'numSlouch' : 0},
                        {'date' : datetime.date, 'numSlouch' : 0},
                        {'date' : datetime.date, 'numSlouch' : 0},
                        {'date' : datetime.date, 'numSlouch' : 1}]}
        firebaseDB.child('users').child(user['email']).set(data)
    else:
        #UPDATE data value
        data = users.val()
        if data[6]['numSlouch'] != datetime.date:
            #add new day to list
            for i in range(0, 5):
                data[i] = data[i+1]
            data[6] = {'date' : datetime.date, 'numSlouch' : 1}
        else:
            data[6]['numSlouch'] = data[6]['numSlouch'] + 1
        firebaseDB.child('users').child(user['email']).update(data)
