from typing import Optional
from app.domain.entities.recipe import Recipe
from app.domain.repositories.recipe_repository import RecipeRepository


class GetRecipeUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def execute(self, recipe_id: int) -> Optional[Recipe]:
        return self.recipe_repository.get_by_id(recipe_id)

