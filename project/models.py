from flask_login import UserMixin
from . import db
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
