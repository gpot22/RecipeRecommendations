from flask import Blueprint, render_template, request, flash
from src import supabase

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
            print(ingredients)
        
        # get array of dics from db
        results = []
        return render_template("home.html",display=results)
