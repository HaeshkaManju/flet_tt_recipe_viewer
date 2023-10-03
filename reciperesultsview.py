import flet as ft
import db_calls

class RecipeResultsView(ft.UserControl):
    def build(self):
        self.header_results = ft.Text("Your Recipe Results")

        