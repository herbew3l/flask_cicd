
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from sqlalchemy import MetaData

from flask import Flask, render_template, request, flash, redirect, session
from flask_sqlalchemy  import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

                         
from flask_cicd.apps.homes.controls import homebp
from flask_cicd.apps.logins.controls import loginbp


# Set App
app = Flask(__name__, template_folder="templates")

Bootstrap(app)

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/db_flask_cicd.db'
app.config['SECRET_KEY'] = "$HERBEWscKKwwqy#@!"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)

app.register_blueprint(homebp)
app.register_blueprint(loginbp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    from flask_cicd.apps.logins.models.users import User
    return User.query.get(int(user_id))

@app.route("/")
def main():
    return redirect('/users/list')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)