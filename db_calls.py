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
    rows = []
    results = session.query(Recipe).all()
    for r in results:
        rows.append(r)
    return rows

def search_recipes_by_name(search_text):
    results = session.query(Recipe).filter(Recipe.name.like(f'%{search_text}%')).all()
    for r in results:
        print(r)
    return results