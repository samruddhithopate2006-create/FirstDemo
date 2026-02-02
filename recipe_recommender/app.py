from flask import Flask, render_template, request

app = Flask(__name__)

# Simple recipe database
recipes = {
    "omelette": {
        "ingredients": ["egg", "onion", "salt"],
        "steps": "Beat eggs, add onion and salt, cook on pan."
    },
    "fried rice": {
        "ingredients": ["rice", "oil", "salt"],
        "steps": "Heat oil, add rice and salt, fry well."
    },
    "salad": {
        "ingredients": ["tomato", "onion", "salt"],
        "steps": "Chop vegetables, add salt, mix well."
    }
}

def get_recipe(user_ingredients):
    user_ingredients = [i.strip().lower() for i in user_ingredients.split(",")]
    
    for recipe, data in recipes.items():
        if all(item in user_ingredients for item in data["ingredients"]):
            return f"{recipe.title()}:\n{data['steps']}"
    
    return "No matching recipe found. Try different ingredients."

@app.route("/", methods=["GET", "POST"])
def home():
    recipe = ""
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        recipe = get_recipe(ingredients)
    return render_template("index.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)
