from flask import render_template, redirect, Blueprint, request
from flask_login import login_required
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .models import Avatars_of_skins
from .data import db_session
from .models import User

main = Blueprint('main', __name__)
db = SQLAlchemy()
api = Api(main)


@main.route('/')
def index():
    return render_template("index.html", nick=User.query.all())


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


@main.route('/invoker')
def invoker_set():
    db_sess = db_session.create_session()
    return render_template('invoker.html')


@main.route('/bloodseeker')
def bloodseeker_set():
    db_sess = db_session.create_session()
    return render_template('bloodseeker.html')


@main.route('/earthshaker')
def earthshaker_set():
    db_sess = db_session.create_session()
    return render_template('earthshaker.html')


@main.route('/enigma')
def enigma_set():
    db_sess = db_session.create_session()
    return render_template('enigma.html')


@main.route('/phantom_lancer')
def phantom_lancer_set():
    db_sess = db_session.create_session()
    return render_template('phantom_lancer.html')


@main.route('/')
def money():
    db_sess = db_session.create_session()
    return redirect("https://winline.ru/")


@main.route('/search',  methods=['POST', 'GET'])
def searching():
    args = request.args.get("search")
    avatars_of_skins = Avatars_of_skins.query.filter_by(hero_name=args).one()
    return redirect(f"/{avatars_of_skins.hero_name}")
