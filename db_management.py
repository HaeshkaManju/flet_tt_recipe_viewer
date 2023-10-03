# db_management.py
import sqlite3
import db_calls

########################################################################################
### BEGIN SECTION ###
# Conection Helper Functions #
### BEGIN SECTION ###
########################################################################################
DB_LOC = "recipes.db"
def helper_connection():
    '''
    Helper function to shortcut the other code.  Just import this
    into every other usage where we ask to look at the database.
    '''
    conn = sqlite3.connect(DB_LOC)
    curs = conn.cursor()
    return conn, curs

def conn_to_db(query_string):
    '''
        Use this as your baseline for connecting to the database.
    '''
    conn, curs = helper_connection()
    res = curs.execute(query_string)
    unprocessed_results = res.fetchall()
    conn.close()
    return unprocessed_results

def tuple_to_list(x):
    '''
    The Database is going to return a list from the individual tuples.
    Use whenever we need to have a list of lists from our DB calls.
    '''
    if type(x) == tuple:
        return list(x)
    elif type(x) == str:
        return [x]
    return "something derpy happened."

########################################################################################
### END OF SECTION ###
# Conection Helper Functions #
### END OF SECTION ###
########################################################################################

########################################################################################
### BEGIN SECTION ###
# Cleaning our data from a query.
### BEGIN SECTION ###
########################################################################################

def first_pass(unprocessed_results):
    print(unprocessed_results)
    # convert from a tuple surrounding a list to a list surrounding a list.
    ## In some instances we may be fine with processing the nested lists.
    ### Harder to do with tuples.  Or, more accurately: we can use the same code
    #### functions for lists.
    first_pass_processing_results = [tuple_to_list(x) for x in unprocessed_results]
    # 
    print("Results of first pass: ")
    print(first_pass_processing_results)
    # Strip away the lists.
    return first_pass_processing_results

def second_pass(first_pass_results):
    '''
        Use this function to clean the lists when you only have one ROW result.
    '''
    print("Prepping for second pass, our data is: ")
    print(first_pass_results)
    for row in first_pass_results:
        processed_strings = [str(r) for r in row]
        print(", ".join(processed_strings))
    return processed_strings

def second_pass_multiline(first_pass_results):
    '''
        Use this function to clean the lists when you only have multiple ROW results.
    '''
    print("our first pass results were: ")
    print(first_pass_results)
    i = 0
    processed_list = []
    while i < len(first_pass_results):
        print(first_pass_results[i])
        processed_list.append(first_pass_results[i][1])
        i+=1
    return processed_list

def second_pass_types(first_pass_results):
    '''
        Use this function to clean the lists when you only have multiple ROW results.
            Specifically for the TYPES table.  We only process a single column,
            so this function essentially grabs "X by 1" instead of "X by Y".
    '''
    print("our first pass results were: ")
    print(first_pass_results)
    i = 0
    processed_list = []
    while i < len(first_pass_results):
        print(first_pass_results[i])
        processed_list.append(first_pass_results[i][0])
        i+=1
    return processed_list

########################################################################################
### END OF SECTION ###
# Cleaning our data from a query.
### END OF SECTION ###
########################################################################################
u = conn_to_db(db_calls.type_query_string)
a = first_pass(u)
print(a)
a = second_pass_types(a)
print(a)