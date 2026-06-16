from app.domain.repositories.ingredient_image_repository import IngredientImageRepository


class DeleteIngredientImageUseCase:
    def __init__(self, ingredient_image_repository: IngredientImageRepository):
        self.ingredient_image_repository = ingredient_image_repository

    def execute(self, image_id: int) -> None:
        ingredient_image = self.ingredient_image_repository.get_by_id(image_id)
        if not ingredient_image:
            raise ValueError("Ingredient image not found")
        
        self.ingredient_image_repository.delete(image_id)

