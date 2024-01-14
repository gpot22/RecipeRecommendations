import ast
from flask import Blueprint, render_template, request
from website.data_table import supabase

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.data:
            ingredients = request.get_json()
        if ingredients:
            ingredients = ast.literal_eval(ingredients)
            print(ingredients)
        
        # get array of dics from db
        recipes = supabase.table("recipe2").select('*').contains('NER', ingredients).execute().data # return dish object(s) based on ingredients
        # print(recipes)
        print(render_template("home.html",recipes=recipes))
    return render_template("home.html", recipes=[{'id': 1000, 'name': 'Salted Peanut Cookies', 'ingredients': ['1 c. shortening (part butter)', '1 1/2 c. brown sugar, packed', '2 eggs', '2 tsp. vanilla', '3 c. flour', '1 tsp. salt', '1/2 tsp. soda', '2 c. salted peanuts'], 'directions': ['Mix butter, sugar, eggs and vanilla thoroughly.', 'Blend rest of ingredients.', 'Drop by rounded teaspoonfuls, about 2 inches apart, on lightly greased sheet.', 'Flatten with bottom of glass dipped in sugar.', 'Bake 8 to 10 minutes at 375°.'], 'link': 'www.cookbooks.com/Recipe-Details.aspx?id=526464', 'source': 'Gathered', 'NER': ['shortening', 'brown sugar', 'eggs', 'vanilla', 'flour', 'salt', 'soda', 'peanuts']}])

# @views.route('/results', methods=["GET", "POST"])
# def test():
    
