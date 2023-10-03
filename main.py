# Main
import flet as ft
from searchview import SearchView

def main(page: ft.Page):
    page.title = "Meal Planner"
    page.update()

    base_search_view = SearchView()
    page.add(base_search_view)


ft.app(port=8550, target=main, view=ft.AppView.WEB_BROWSER)