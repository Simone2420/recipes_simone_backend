from typing import Optional
from app.domain.entities.ingredient import Ingredient
from app.domain.repositories.ingredient_repository import IngredientRepository


class GetIngredientUseCase:
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    def execute(self, ingredient_id: int) -> Optional[Ingredient]:
        return self.ingredient_repository.get_by_id(ingredient_id)

