from app.domain.entities.ingredient import Ingredient
from app.domain.repositories.ingredient_repository import IngredientRepository
from app.application.dtos.ingredient.update_ingredient_dto import UpdateIngredientDTO


class UpdateIngredientUseCase:
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    def execute(self, ingredient_id: int, dto: UpdateIngredientDTO) -> Ingredient:
        ingredient = self.ingredient_repository.get_by_id(ingredient_id)
        if not ingredient:
            raise ValueError("Ingredient not found")
        
        if dto.name is not None:
            ingredient.name = dto.name
        
        return self.ingredient_repository.save(ingredient)

