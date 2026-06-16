from app.domain.entities.ingredient_image import IngredientImage
from app.domain.repositories.ingredient_image_repository import IngredientImageRepository
from app.application.dtos.ingredient_image.create_ingredient_image_dto import CreateIngredientImageDTO


class CreateIngredientImageUseCase:
    def __init__(self, ingredient_image_repository: IngredientImageRepository):
        self.ingredient_image_repository = ingredient_image_repository

    def execute(self, dto: CreateIngredientImageDTO) -> IngredientImage:
        ingredient_image = IngredientImage(
            id=0,
            image_url=dto.image_url,
            ingredient_id=dto.ingredient_id
        )
        return self.ingredient_image_repository.save(ingredient_image)

