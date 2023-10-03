# Main
import flet as ft
from searchview import SearchView
from reciperesultsview import RecipeResultsView

def main(page: ft.Page):
    page.title = "Meal Planner"
    page.update()

    base_search_view = SearchView()
    page.add(base_search_view)

    search_results_found = False
    
    base_recipe_view = RecipeResultsView()
    page.add(base_recipe_view)


ft.app(port=8550, target=main, view=ft.AppView.WEB_BROWSER)