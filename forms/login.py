from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(gettext('Email', validators=[DataRequired()]))
    password = PasswordField(gettext('Password', validators=[DataRequired()]))
    remember_me = BooleanField(gettext('Remember'))
    submit = SubmitField(gettext('Login'))