from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .models import User
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from flask_babel import Babel
from .models import Gifs_of_skins

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        return 'ru'

    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
