import ast
from flask import Blueprint, render_template, request
from website.data_table import supabase
import random
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", recipes=[], user=current_user)

@views.route('/', methods=["GET", "POST"])
def update_recipes():
    if request.method == "POST":
        if request.data:
            ingredients = request.get_json()
        if ingredients:
            ingredients = ast.literal_eval(ingredients)
        recipes = supabase.table("recipe2").select('*').contains('NER', ingredients).execute().data # return dish object(s) based on ingredients
        random.shuffle(recipes)  # randomize query order to give user some variety and simulate what it might be like if we were to use ML
        return render_template("home.html",recipes=recipes, ingredients=ingredients, query=True, user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)