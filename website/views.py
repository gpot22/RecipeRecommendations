from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/results')
def test():
    results = [["Pie",["sugar","idk"],["bake it"],"getbootstrap.com/docs/4.0/components/card/#titles-text-and-links"],["Fire Noodles",["noodles","sauce"],["boil water and add noodles","add sauce"],""]]
    return render_template("results.html",display=results)