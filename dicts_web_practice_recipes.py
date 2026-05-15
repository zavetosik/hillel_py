import requests
from pprint import pprint

url_recipes = 'https://dummyjson.com/recipes'
params = {
    "skip": 0,
    "limit": 1000,
}

response = requests.get(url=url_recipes, params=params)
recipes = response.json()['recipes']


pizza_recipes = []
italian_count = 0
max_calories = 0
max_recipe = None
recipes_190 = []
total_reviews = 0


for recipe in recipes:
    # pizza recipes
    if "pizza" in recipe['name'].lower():
        pizza_recipes.append(recipe)

    # italian count
    if recipe['cuisine'] == 'Italian':
        italian_count += 1

    # max calories
    if recipe['caloriesPerServing'] > max_calories:
        max_calories = recipe['caloriesPerServing']
        max_recipe = recipe

    # instructions with 190
    if recipe['instructions']:
        if "190" in recipe['instructions'][0]:
            recipes_190.append(recipe)

    # total reviews
    total_reviews += recipe['reviewCount']
