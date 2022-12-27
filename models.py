from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_msearch import Search

db = SQLAlchemy()
search = Search(db=db)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Avatars_of_skins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_name = db.Column(db.String(100))
    image_link = db.Column(db.String(100))


class Gifs_of_skins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_name = db.Column(db.String(100))
    gif_link = db.Column(db.String(100))
