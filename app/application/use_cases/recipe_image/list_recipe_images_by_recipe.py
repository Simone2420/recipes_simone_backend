from typing import List
from app.domain.entities.recipe_image import RecipeImage
from app.domain.repositories.recipe_image_repository import RecipeImageRepository


class ListRecipeImagesByRecipeUseCase:
    def __init__(self, recipe_image_repository: RecipeImageRepository):
        self.recipe_image_repository = recipe_image_repository

    def execute(self, recipe_id: int) -> List[RecipeImage]:
        return self.recipe_image_repository.get_by_recipe_id(recipe_id)

