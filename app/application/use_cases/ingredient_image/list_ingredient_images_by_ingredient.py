from typing import List
from app.domain.entities.ingredient_image import IngredientImage
from app.domain.repositories.ingredient_image_repository import IngredientImageRepository


class ListIngredientImagesByIngredientUseCase:
    def __init__(self, ingredient_image_repository: IngredientImageRepository):
        self.ingredient_image_repository = ingredient_image_repository

    def execute(self, ingredient_id: int) -> List[IngredientImage]:
        return self.ingredient_image_repository.get_by_ingredient_id(ingredient_id)

