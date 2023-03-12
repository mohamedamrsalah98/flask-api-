from flask import render_template
from app.models import Categories
from app.category import Categ_blueprint


@Categ_blueprint.route('/')
def category_index():
    categories = Categories.get_all_categories()
    return render_template('category/category.html', categories=categories)
