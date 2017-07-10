from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
from moduleGlobal import app

# app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config')
# app.config.from_pyfile('localConfig.py')
db = SQLAlchemy(app)


# db


class Gzh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    img = db.Column(db.String(120))
    created_at = db.Column(db.String(120))
    url = db.Column(db.String(120))
    status = db.Column(db.String(120))

    def __init__(self, name='', img='', created_at='', url='',status="published"):
        self.name = name
        self.img = img
        self.url = url
        self.created_at = time.time()
        self.status = status

    def __repr__(self):
        return '<Gzh %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    auth = db.Column(db.String(120))
    password = db.Column(db.String(120))

    def __init__(self, name='', auth=1, password=''):
        self.name = name
        self.auth = auth
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


