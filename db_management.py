import sqlite3
from sqlalchemy import create_engine, ForeignKey, Table, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()

DB_LOC = """F:\Github\\flet_tt_recipe_viewer\\recipes.db"""

##############################################################################
### BEGIN SECTION ###
# XREF #
### BEGIN SECTION ###
##############################################################################

recipes_types = Table("recipes_types_XREF", 
                         Base.metadata, 
                         Column("recipe_id", Integer, ForeignKey("recipes.id")),
                         Column("type_id", Integer, ForeignKey("types.id")), 
                         )

recipes_ingredients = Table("recipes_ingredients_XREF", 
                         Base.metadata, 
                         Column("recipe_id", Integer, ForeignKey("recipes.id")),
                         Column("ingredient_id", Integer, ForeignKey("ingredients.id")), 
                         )

##############################################################################
### END SECTION ###
# XREF #
### END SECTION ###
##############################################################################

##############################################################################
### BEGIN SECTION ###
# Type Class Definition #
### BEGIN SECTION ###
##############################################################################
class Type(Base):
    __tablename__ ='types'

    id = Column('id', Integer, primary_key = True)
    type = Column('type', String)
    recipes = relationship('Recipe', secondary=recipes_types, back_populates='type')

    def __repr__(self):
        return f"Type(id={self.id}, type={self.type})"
    
    def __str__(self):
        return f"{self.type}"

##############################################################################
### END OF SECTION ###
# Type Class Definition #
### END OF SECTION ###
##############################################################################

##############################################################################
### BEGIN SECTION ###
# Ingredient Class Definition #
### BEGIN SECTION ###
##############################################################################
class Ingredient(Base):
    __tablename__ ='ingredients'

    id = Column('id', Integer, primary_key = True)
    ingredient = Column('ingredient', String)
    store = Column('store', Integer)
    recipes = relationship('Recipe', secondary=recipes_ingredients, back_populates='ingredients')

    def __repr__(self):
        return f"Ingredient(id={self.id}, ingredient={self.ingredient}, store={self.store})"
    
    def __str__(self):
        return f"{self.ingredient}"

##############################################################################
### END OF SECTION ###
# Ingredient Class Definition #
### END OF SECTION ###
##############################################################################

##############################################################################
### BEGIN SECTION ###
# Recipe Class Definition #
### BEGIN SECTION ###
##############################################################################
class Recipe(Base):
    __tablename__ ='recipes'

    recipe_id = Column('id', Integer, primary_key = True)
    name = Column('name', String)
    score = Column('score', Integer)
    image_loc = Column('image_loc', String)
    link = Column('link', String)
    type = relationship('Type', secondary=recipes_types, back_populates='recipes')
    ingredients = relationship('Ingredient', secondary=recipes_ingredients, back_populates='recipes')

    def __repr__(self):
        return f"Recipe(recipe_id={self.recipe_id}, name={self.name}, score={self.score}, image_loc={self.image_loc}, link={self.link}, type={self.type}, ingredients={self.ingredients})"

    def __str__(self):
        ingredients = ""
        for item in self.ingredients:
            ingredients += "\t"
            ingredients += str(item)
            ingredients += "\n"
        type = ""
        for item in self.type:
            type += str(item)
        string = f"""
# {self.name} #
id: {self.recipe_id}
score: {self.score}
image_loc: {self.image_loc}
link: {self.link}
type: {type}
ingredients: 
{ingredients}"""
        return string

##############################################################################
### END OF SECTION ###
# Recipe Class Definition #
### END OF SECTION ###
##############################################################################

##############################################################################
### BEGIN SECTION ###
# Engine & Session creation #
### BEGIN SECTION ###
##############################################################################

engine = create_engine('sqlite:///' + DB_LOC, echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

##############################################################################
### END OF SECTION ###
# Engine & Session creation #
### END OF SECTION ###
##############################################################################

##############################################################################
### BEGIN SECTION ###
# Testing #
### BEGIN SECTION ###
##############################################################################
'''
def testing():
    results = session.query(Recipe).all()
    for r in results:
        print(r)

testing()
'''
##############################################################################
### END OF SECTION ###
# Testing #
### END OF SECTION ###
##############################################################################
