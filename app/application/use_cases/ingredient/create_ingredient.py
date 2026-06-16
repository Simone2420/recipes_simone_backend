from app.domain.entities.ingredient import Ingredient
from app.domain.repositories.ingredient_repository import IngredientRepository
from app.application.dtos.ingredient.create_ingredient_dto import CreateIngredientDTO


class CreateIngredientUseCase:
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    def execute(self, dto: CreateIngredientDTO) -> Ingredient:
        ingredient = Ingredient(
            id=0,
            name=dto.name,
            recipe_id=dto.recipe_id
        )
        return self.ingredient_repository.save(ingredient)

