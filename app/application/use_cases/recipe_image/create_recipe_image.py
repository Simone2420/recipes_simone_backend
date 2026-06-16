from app.domain.entities.recipe_image import RecipeImage
from app.domain.repositories.recipe_image_repository import RecipeImageRepository
from app.application.dtos.recipe_image.create_recipe_image_dto import CreateRecipeImageDTO


class CreateRecipeImageUseCase:
    def __init__(self, recipe_image_repository: RecipeImageRepository):
        self.recipe_image_repository = recipe_image_repository

    def execute(self, dto: CreateRecipeImageDTO) -> RecipeImage:
        recipe_image = RecipeImage(
            id=0,
            image_url=dto.image_url,
            recipe_id=dto.recipe_id
        )
        return self.recipe_image_repository.save(recipe_image)

