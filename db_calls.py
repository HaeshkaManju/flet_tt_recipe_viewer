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