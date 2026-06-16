from app.domain.entities.recipe_image import RecipeImage
from app.domain.repositories.recipe_image_repository import RecipeImageRepository
from app.application.dtos.recipe_image.update_recipe_image_dto import UpdateRecipeImageDTO


class UpdateRecipeImageUseCase:
    def __init__(self, recipe_image_repository: RecipeImageRepository):
        self.recipe_image_repository = recipe_image_repository

    def execute(self, image_id: int, dto: UpdateRecipeImageDTO) -> RecipeImage:
        recipe_image = self.recipe_image_repository.get_by_id(image_id)
        if not recipe_image:
            raise ValueError("Recipe image not found")
        
        if dto.image_url is not None:
            recipe_image.image_url = dto.image_url
        
        return self.recipe_image_repository.save(recipe_image)

