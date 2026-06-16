from typing import Optional
from app.domain.entities.ingredient_image import IngredientImage
from app.domain.repositories.ingredient_image_repository import IngredientImageRepository


class GetIngredientImageUseCase:
    def __init__(self, ingredient_image_repository: IngredientImageRepository):
        self.ingredient_image_repository = ingredient_image_repository

    def execute(self, image_id: int) -> Optional[IngredientImage]:
        return self.ingredient_image_repository.get_by_id(image_id)

