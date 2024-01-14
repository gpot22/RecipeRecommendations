import ast
from flask import Blueprint, render_template, request
from website.data_table import supabase

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/results', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        if request.data:
            ingredients = request.get_json()
        if ingredients:
            ingredients = ast.literal_eval(ingredients)
        
        # get array of dics from db
        recipes = supabase.table("recipe2").select('*').contains('NER', ingredients).execute() # return dish object(s) based on ingredients
        print(recipes)
        return render_template("home.html",display=recipes)
