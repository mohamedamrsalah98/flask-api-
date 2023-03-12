from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Post,Categories
from wtforms.widgets import CheckboxInput
from wtforms import BooleanField


class PostForm(FlaskForm):
    title = StringField('title')
    body = StringField('body')



class CategoryForm(FlaskForm):
    name = StringField('Category Name')






