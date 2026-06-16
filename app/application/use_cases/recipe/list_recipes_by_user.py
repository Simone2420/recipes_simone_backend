from typing import List
from app.domain.entities.recipe import Recipe
from app.domain.repositories.recipe_repository import RecipeRepository


class ListRecipesByUserUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def execute(self, user_id: int) -> List[Recipe]:
        return self.recipe_repository.get_by_user_id(user_id)

