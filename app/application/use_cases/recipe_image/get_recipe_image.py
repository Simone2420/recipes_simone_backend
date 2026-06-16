from typing import Optional
from app.domain.entities.recipe_image import RecipeImage
from app.domain.repositories.recipe_image_repository import RecipeImageRepository


class GetRecipeImageUseCase:
    def __init__(self, recipe_image_repository: RecipeImageRepository):
        self.recipe_image_repository = recipe_image_repository

    def execute(self, image_id: int) -> Optional[RecipeImage]:
        return self.recipe_image_repository.get_by_id(image_id)

