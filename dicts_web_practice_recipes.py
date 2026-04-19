import requests
from pprint import pprint

url_recipes = 'https://dummyjson.com/recipes'
params = {
    "skip": 0,
    "limit": 1000,
}

response = requests.get(url=url_recipes, params=params)
response_json = response.json()

recipes = response_json['recipes']


pizza_recipes = []
for recipe in recipes:
    if "pizza" in recipe['name']:
        pizza_recipes.append(recipe)



italian_count = 0
for recipe in recipes:
    if recipe['cuisine'] == 'Italian':
        italian_count += 1



max_calories = 0
max_recipe = None

for recipe in recipes:
    if recipe['caloriesPerServing'] > max_calories:
        max_calories = recipe['caloriesPerServing']
        max_recipe = recipe



recipes_190 = []

for recipe in recipes:
    if len(recipe['instructions']) > 0:
        first_instruction = recipe['instructions'][0]
        if "190" in first_instruction:
            recipes_190.append(recipe)



total_reviews = 0

for recipe in recipes:
    total_reviews += recipe['reviewCount']