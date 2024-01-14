from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    # find recipes when button is pressed
    if request.method == "POST":
        ingredients = request.args.get("ingredientList")
        print(ingredients)
        if ingredients:
            # need recipes variable that checks data base for recipes with all ingredients
            recipes = [["Pie",["sugar","idk"],["bake it"],"getbootstrap.com/docs/4.0/components/card/#titles-text-and-links"],["Fire Noodles",["noodles","sauce"],["boil water and add noodles","add sauce"],""]]

            # Send recipe list to the page
            # Could also save ingredients through session; could be glitchy due to nature of flask
            return render_template("home.html", ingredients=ingredients, recipes=recipes)
        else:
            flash('No ingredients entered')
    
    return render_template("home.html", ingredients=[])

@views.route('/results', methods=["GET", "POST"])
def test():
    if request.method == "POST":
        if request.data:
            ingredients = request.get_json()
        if ingredients:
            print(ingredients)
        results = [["Pie",["sugar","idk"],["bake it"],"getbootstrap.com/docs/4.0/components/card/#titles-text-and-links"],["Fire Noodles",["noodles","sauce"],["boil water and add noodles","add sauce"],""]]
        return render_template("home.html",display=results)
