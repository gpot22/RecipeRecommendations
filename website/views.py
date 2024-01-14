from flask import Blueprint, render_template, request, flash
from src import supabase

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    # find recipes when button is pressed
    if request.method == "POST":
        ingredients = list(map(str.strip,request.form['search'].split(',')))
        if ingredients:
            # need recipes variable that checks data base for recipes with all ingredients
            # recipes = ["queried recipes"]
            ingr = supabase.table("recipe2").select('*').contains('NER', ingredients).execute().data
            recipes = []
            for i in ingr:
                rec = []
                rec.append(i["name"])
                rec.append(i["ingredients"])
                rec.append(i["directions"])
                rec.append(i["link"])
                rec.append(i["id"])
                recipes.append(rec)

            # Send recipe list to the page
            # Could also save ingredients through session; could be glitchy due to nature of flask
            return render_template("home.html", ingredients=ingredients, recipes=recipes)
        else:
            flash('No ingredients entered')
    
    return render_template("home.html", ingredients=[])

@views.route('/results')
def test():
    results = [["Pie",["sugar","idk"],["bake it"],"getbootstrap.com/docs/4.0/components/card/#titles-text-and-links"],["Fire Noodles",["noodles","sauce"],["boil water and add noodles","add sauce"],""]]
    return render_template("results.html",display=results)
