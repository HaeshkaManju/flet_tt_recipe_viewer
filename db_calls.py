# db_calls.py

################################
# All TYPES-related Calls
################################
type_name = None
types_call = """SELECT types.type FROM types;"""
types_input = """INSERT INTO types (type) VALUES (?);"""
recipe_name = None


verify_tables_query_string = "SELECT * FROM sqlite_master WHERE type='table';"
recipe_query_string = f"SELECT * FROM recipes WHERE name = '{recipe_name}';".format(recipe_name)
recipe_type_XREF_query_string = f'''SELECT recipes.name, types.type FROM recipes INNER JOIN recipes_types_XREF ON recipes.id = recipes_types_XREF.recipe_id INNER JOIN types ON recipes_types_XREF.type_id = types.id WHERE name = '{recipe_name}';'''.format(recipe_name)
recipe_ingredient_XREF_query_string = f'''SELECT recipes.name, ingredients.ingredient FROM recipes INNER JOIN recipes_ingredients_XREF ON recipes.id = recipes_ingredients_XREF.recipe_id INNER JOIN ingredients ON recipes_ingredients_XREF.ingredient_id = ingredients.id WHERE name = '{recipe_name}';'''.format(recipe_name)
type_query_string = '''SELECT types.type AS type FROM types;'''