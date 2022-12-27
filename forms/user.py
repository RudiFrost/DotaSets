from flask_babel import gettext
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField(gettext('Email', validators=[DataRequired()]))
    password = PasswordField(gettext('Password', validators=[DataRequired()]))
    password_again = PasswordField(gettext('Repeat password', validators=[DataRequired()]))
    name = StringField(gettext('Username', validators=[DataRequired()]))
    about = TextAreaField(gettext("Something about you"))
    submit = SubmitField(gettext('Submit'))
