from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    # find recipes when button is pressed
    if request.method == "POST":
        ingredients = request.args.get("ingredients")
        
        # need recipes variable that checks data base for recipes with all ingredients
        recipes = ["queried recipes"]

        # Send recipe list to the page
        # Could also save ingredients through session; could be glitchy due to nature of flask
        return render_template("home.html", foods = zip(ingredients, recipes))
    
    return render_template("home.html")

@views.route('/results')
def test():
    results = [["Pie",["sugar","idk"],["bake it"],"getbootstrap.com/docs/4.0/components/card/#titles-text-and-links"],["Fire Noodles",["noodles","sauce"],["boil water and add noodles","add sauce"],""]]
    return render_template("results.html",display=results)
