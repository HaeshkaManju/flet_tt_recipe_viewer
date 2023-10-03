# db_calls.py
from db_management import *


################################
# All TYPES-related Calls
################################


def call_types():
    results = session.query(Type).all()
    for r in results:
        print(r)
    return results


def call_recipes():
    results = session.query(Recipe).all()
    for r in results:
        print(r)
    return results


def search_recipes_by_name(search_text):
    results = session.query(Recipe).filter(Recipe.name.like(f'%{search_text}%')).all()
    for r in results:
        print(r)
    print(results)
    return results


def search_recipes_by_type(search_type):
    results = session.query(Recipe).filter(Recipe.type_id == search_type).all()
    for r in results:
        print(r)
    return results


def search_recipes_by_ingredient(search_ingredients, require_all=False):
    all_recipe_matches = []
    for ingredient in search_ingredients:
        ingredient_objects = session.query(Ingredient).filter(Ingredient.ingredient.like(f'%{ingredient}%')).all()
        for object in ingredient_objects:
            recipe_matches = object.recipes
            for recipe in recipe_matches:
                all_recipe_matches.append(recipe)

    counted_recipe_matches = []
    for recipe in all_recipe_matches:
        count = all_recipe_matches.count(recipe)
        counted_recipe_matches.append((count, recipe))

    sorted_recipe_matches = []
    for item in counted_recipe_matches:
        if item not in sorted_recipe_matches:
            sorted_recipe_matches.append(item)

    sorted_recipe_matches.sort(key=lambda x: x[0], reverse=True)

    results = []
    for item in sorted_recipe_matches:
        if require_all and item[0] == len(search_ingredients):
            results.append(item[1])
        elif not require_all:
            results.append(item[1]) 

    for r in results:
        print(r)
    return results
