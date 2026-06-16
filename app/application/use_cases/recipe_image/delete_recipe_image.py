from app.domain.repositories.recipe_image_repository import RecipeImageRepository


class DeleteRecipeImageUseCase:
    def __init__(self, recipe_image_repository: RecipeImageRepository):
        self.recipe_image_repository = recipe_image_repository

    def execute(self, image_id: int) -> None:
        recipe_image = self.recipe_image_repository.get_by_id(image_id)
        if not recipe_image:
            raise ValueError("Recipe image not found")
        
        self.recipe_image_repository.delete(image_id)

