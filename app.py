from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "YOUR_SPOONACULAR_API_KEY"  
BASE_URL = "https://ai-food-recipe-generator-api-custom-diet-quick-meals.p.rapidapi.com/generate?noqueue=1"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return render_template("index.html", error="Please enter a search term.")

 
    url = f"{BASE_URL}/complexSearch"
    params = {
        "apiKey": API_KEY,
        "query": query,
        "number": 10, 
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        return render_template("index.html", error="No recipes found.")

    recipes = data["results"]
    return render_template("index.html", recipes=recipes)

@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
  
    url = f"{BASE_URL}/{recipe_id}/information"
    params = {
        "apiKey": API_KEY,
    }
    response = requests.get(url, params=params)
    recipe = response.json()

    return render_template("recipe.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)