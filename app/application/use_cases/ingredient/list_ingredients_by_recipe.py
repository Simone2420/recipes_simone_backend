from typing import List
from app.domain.entities.ingredient import Ingredient
from app.domain.repositories.ingredient_repository import IngredientRepository


class ListIngredientsByRecipeUseCase:
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    def execute(self, recipe_id: int) -> List[Ingredient]:
        return self.ingredient_repository.get_by_recipe_id(recipe_id)

