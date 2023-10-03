import flet as ft
import db_calls


class RecipeResultsView(ft.UserControl):
    def build(self):
        self.header_results = ft.Text("Your Recipe Results")
        self.recipe_results = []
        self.recipe_cards = []

        for recipe in self.recipe_results:
            recipe_card = self.create_recipe_card(recipe)
            self.recipe_cards.append(recipe_card)

        ###########################
        # The Recipe Results View #
        ###########################
        recipe_results_view = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.header_results
                    ]
                ),
                ft.Column(
                    controls=[card for card in self.recipe_cards]
                )
                
            ]
        )

        return recipe_results_view
    
    def create_recipe_card(self, recipe):
        recipe_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(recipe)
                    ]
                ),
                width=600,
                padding=10,
            )
        )


