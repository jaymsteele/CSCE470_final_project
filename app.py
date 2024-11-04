from flask import Flask, render_template, request, jsonify
import pandas as pd
import json
from bm25 import BM25
# Initialize the Flask app
app = Flask(__name__)

# Load the recipes dataset
recipes = pd.read_csv('data/RAW_recipes.csv')

# Load unique ingredients from JSON
with open('data/ingredients.json', 'r') as f:
    unique_ingredients = json.load(f)

# Preprocess and tokenize the ingredients
def preprocess_ingredients(ingredients):
    ingredients_list = eval(ingredients) if isinstance(ingredients, str) else []
    return [ingredient.lower() for ingredient in ingredients_list]

recipes['tokenized_ingredients'] = recipes['ingredients'].apply(preprocess_ingredients)

# Initialize custom BM25 model with tokenized ingredients
bm25_model = BM25(recipes['tokenized_ingredients'].tolist())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ingredients')
def get_ingredients():
    return jsonify(unique_ingredients)

@app.route('/search', methods=['POST'])
def search():
    # Get all user-submitted ingredients
    user_ingredients = request.form.getlist('ingredients')
    tokenized_user_ingredients = [item.lower() for item in user_ingredients if item]
    
    # Get BM25 scores for the user-selected ingredients
    scores = bm25_model.get_scores(tokenized_user_ingredients)
    recipes['bm25_score'] = scores

    # Rank recipes by BM25 score and select top 5
    ranked_recipes = recipes.sort_values(by='bm25_score', ascending=False).head(5)
    top_recipes = ranked_recipes[['name', 'ingredients', 'bm25_score']].to_dict(orient='records')
    
    return render_template('results.html', recipes=top_recipes)

if __name__ == '__main__':
    app.run(debug=True)
