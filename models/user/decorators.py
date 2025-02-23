import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app


def requires_login(f: Callable) -> Callable:
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        # *args, **kwargs means it accepts any amount of arguments
        # and any amount of keyword arguments
        if not session.get('email'):
            flash('You need to be signed in for this page.', 'danger')
            # flash places the messages in a queue
            return redirect(url_for('users.login_user'))
        return f(*args, **kwargs)
    return decorated_function
