from flask import Blueprint, render_template, redirect, url_for, session, request, send_from_directory
from models.user import User, errors, requires_login
from common.utils import Utils

data_blueprint = Blueprint('data', __name__)


@data_blueprint.route('/')
@requires_login
def index():
    return render_template('../client/build/index.html')


@data_blueprint.route('/update', methods=['GET'])
@requires_login
def slouch_update():
    if request.method == 'GET':
        user_data = User.find_by_email(session['email']).val()
        user = User(session['email'], 1234, {'timesSlouched' : user_data.get('timesSlouched')})
        user.update_slouch_data(session['email'])
        user.send_slouch_notif()


@data_blueprint.route('/week', methods=['GET'])
@requires_login
def week_slouch_data():
    if request.method == 'GET':
        data = User.get_slouch_data(session['email'])
        return {'timesSlouched' : data.get('timesSlouched')}


# @data_blueprint.route('/history')
# @requires_login
# def index():
#     return render_template('data/history.html')


# @data_blueprint.route('/analytics')
# @requires_login
# def index():
#     return render_template('data/analytics.html')