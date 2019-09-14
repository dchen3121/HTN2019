from flask import Blueprint, render_template, redirect, url_for, session, request
from models.user import requires_login
from common.utils import Utils

data_blueprint = Blueprint('data', __name__)


@data_blueprint.route('/')
@requires_login
def index():
    return render_template('data/index.html')


# @data_blueprint.route('/history')
# @requires_login
# def index():
#     return render_template('data/history.html')


# @data_blueprint.route('/analytics')
# @requires_login
# def index():
#     return render_template('data/analytics.html')
