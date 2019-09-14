import os
from flask import Flask, redirect, url_for, session, render_template
# from views.some_stuff import ...
import pyrebase

app = Flask(__name__)
app.secret_key = "s7@8ob3fn8$%9nf64o&bv02q84gn74v!o78o34u78#27g4fno49lu*7h87q23fb1ui"
# sample secret key, change in prod
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)
# we might not need this, change later

# app.register_blueprint(alert_blueprint, url_prefix="/...")  # do this later

@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
