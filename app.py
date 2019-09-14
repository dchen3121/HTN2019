import os
from flask import Flask, redirect, url_for, session, render_template
from views.users import user_blueprint
from views.data import data_blueprint

app = Flask(__name__)
app.secret_key = "s7@8ob3fn8$%9nf64o&bv02q84gn74v!o78o34u78#27g4fno49lu*7h87q23fb1ui"
# sample secret key, change in prod
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)
# we might not need this, change later


app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(data_blueprint, url_prefix="/users")


@app.route('/')
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
