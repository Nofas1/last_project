from flask_wtf import FlaskForm
from wtforms import  BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash


class Add_news(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = StringField('Содержание', validators=[DataRequired()])
    submit = SubmitField('Сохранить')