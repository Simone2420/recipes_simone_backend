from app.domain.repositories.ingredient_repository import IngredientRepository


class DeleteIngredientUseCase:
    def __init__(self, ingredient_repository: IngredientRepository):
        self.ingredient_repository = ingredient_repository

    def execute(self, ingredient_id: int) -> None:
        ingredient = self.ingredient_repository.get_by_id(ingredient_id)
        if not ingredient:
            raise ValueError("Ingredient not found")
        
        self.ingredient_repository.delete(ingredient_id)

