import ast
from flask import Blueprint, render_template, request
from website.data_table import supabase

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", recipes=[])

@views.route('/', methods=["GET", "POST"])
def update_recipes():
    if request.method == "POST":
        if request.data:
            ingredients = request.get_json()
        if ingredients:
            ingredients = ast.literal_eval(ingredients)
            print(ingredients)
        recipes = supabase.table("recipe2").select('*').contains('NER', ingredients).execute().data # return dish object(s) based on ingredients
        return render_template("home.html",recipes=recipes, ingredients=ingredients)
    
