import pandas as pd
import json

# Load the recipes dataset
recipes = pd.read_csv('data/RAW_recipes.csv')

# Function to clean and preprocess ingredients
def preprocess_ingredients(ingredients):
    # Convert the string representation of the list to an actual list of ingredients
    ingredients_list = eval(ingredients) if isinstance(ingredients, str) else []
    ingredients_list = [ingredient.strip().lower() for ingredient in ingredients_list]
    return ingredients_list

# Apply the preprocessing function to create a tokenized list of ingredients
recipes['tokenized_ingredients'] = recipes['ingredients'].apply(preprocess_ingredients)

# Extract unique ingredients
all_ingredients = set()
recipes['tokenized_ingredients'].apply(lambda x: all_ingredients.update(x))
unique_ingredients = sorted(all_ingredients)

# Save the unique ingredients to a JSON file
with open('data/ingredients.json', 'w') as f:
    json.dump(unique_ingredients, f, indent=2)

print("ingredients.json has been generated successfully.")
