import random

from flask import render_template, redirect, Blueprint, request
from flask_login import login_required
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from .data import db_session
from .models import User, Gifs_of_skins, Avatars_of_skins
from .test_db import test_abaddon

main = Blueprint('main', __name__)
db = SQLAlchemy()
api = Api(main)


class Heroes(Resource):
    def get(self, id=1):
        heroes = Gifs_of_skins.query.all()
        for name in heroes:
            if (name.id == id):
                return {"id": name.id, "hero_name": name.hero_name}
            if (id  == 0):
                quote = random.choice(heroes)
                return {"id": quote.id, "hero_name": quote.hero_name}
        return "Quote not found"


api.add_resource(Heroes, "/api/heroes", "/api/heroes/random", "/api/heroes/<int:id>")
api.init_app(main)


@main.route('/')
def index():
    avatars = Avatars_of_skins.query.all()
    gifs = Gifs_of_skins.query.all()
    return render_template("index.html", ava=avatars, gif=gifs)


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    db_sess = db_session.create_session()
    return render_template("profile.html", nick=User.query.all())


@main.route('/about')
def about_site():
    db_sess = db_session.create_session()
    return render_template('about.html')


@main.route('/change_password')
def change_password():
    db_sess = db_session.create_session()
    return render_template('profile.html')


@main.route('/<variable>')
def hero(variable):
    avatars = Avatars_of_skins.query.all()
    gifs = Gifs_of_skins.query.all()
    return render_template('hero.html', ava=avatars, gif=gifs)


@main.route('/')
def money():
    db_sess = db_session.create_session()
    return redirect("https://winline.ru/")


@main.route('/search', methods=['POST', 'GET'])
def searching():
    args = request.args.get("search")
    avatars_of_skins = Avatars_of_skins.query.filter_by(hero_name=args).one()
    return redirect(f"/{avatars_of_skins.hero_name}")


@main.route('/test')
def arg():
    test_abaddon()
    return {"time": "time"}