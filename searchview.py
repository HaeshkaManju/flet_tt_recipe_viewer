import flet as ft
import db_calls

class SearchView(ft.UserControl):
    def build(self):
        self.header1 = ft.Text("Search via Recipes, Types, or Ingredients.")

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
        #       Text Labels (ft.Text()     # 
        # are for debugging purposes ONLY! #
        #     Remove in production code!   #
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

        ##########################
        # Recipe Search Controls #
        ##########################
        self.user_recipe_search_label = ft.Text()
        self.user_recipe_input = ft.TextField(
            value="", 
            label="Search Recipes", 
            hint_text="Enter part of a recipe name..."
        )
        recipe_search_button = ft.ElevatedButton(
            text="Submit", 
            on_click=self.button_recipe_search
        )
        ########################
        # Type Search Controls #
        ########################
        self.user_type_search_label = ft.Text()
        self.user_type_input = ft.Dropdown(
            value="", 
            label="Type", 
            hint_text="Select a Type from the list", 
            options=[ft.dropdown.Option(x) for x in db_calls.call_types()], 
            autofocus=False
        )
        type_search_button = ft.ElevatedButton(
            text="Submit", 
            on_click=self.button_type_search
        )
        ###############################
        # Ingredients Search Controls #
        ###############################
        self.user_ingredients_search_label = ft.Text()
        self.user_ingredients_input = ft.TextField(
            value="", 
            label="Enter one Ingredient on each line.", 
            multiline=True, 
            min_lines=1, 
            max_lines=6
        )
        ingredients_search_button = ft.ElevatedButton(
            text="Submit", 
            on_click=self.button_ingredients_search
        )        
        
        ###################
        # The Search View #
        ###################
        search_view = ft.Column(
            width = 600, 
            controls=[
                ft.Row(
                    controls=[
                        self.header1
                    ]
                ), 
                ft.Row(
                    controls=[
                        self.user_recipe_search_label, 
                        self.user_recipe_input, 
                        recipe_search_button
                    ]
                ), 
                ft.Row(
                    controls=[
                        self.user_type_search_label, 
                        self.user_type_input, 
                        type_search_button
                    ]
                ), 
                ft.Row(
                    controls=[
                        self.user_ingredients_search_label, 
                        self.user_ingredients_input, 
                        ingredients_search_button
                    ]
                ) 
            ]
        )

        return search_view

        #!!!!!!!!!#
        '''
            Rewrite these buttons as a single defined function that takes the 
            individual button's and input fields as arguments.
        '''
    def button_recipe_search(self, e):
        # I genuinely do not understand how these buttons work or how the 
        # values are getting updated.
        self.user_recipe_search_label.value = self.user_recipe_input.value
        print(self.user_recipe_search_label.value)
        self.update()
        db_calls.search_recipes_by_name(self.user_recipe_input.value)

    def button_type_search(self, e):
        self.user_type_search_label.value = self.user_type_input.value
        print(self.user_type_search_label.value)
        self.update()

    def button_ingredients_search(self, e):
        self.user_ingredients_search_label.value = \
            self.user_ingredients_input.value
        print(self.user_ingredients_search_label.value)
        self.update()