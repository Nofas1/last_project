from flask_wtf import FlaskForm
from wtforms import PasswordField,  BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash


class Button_add(FlaskForm):
    submit = SubmitField('Добавить')