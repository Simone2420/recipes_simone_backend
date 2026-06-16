from app.domain.entities.ingredient_image import IngredientImage
from app.domain.repositories.ingredient_image_repository import IngredientImageRepository
from app.application.dtos.ingredient_image.update_ingredient_image_dto import UpdateIngredientImageDTO


class UpdateIngredientImageUseCase:
    def __init__(self, ingredient_image_repository: IngredientImageRepository):
        self.ingredient_image_repository = ingredient_image_repository

    def execute(self, image_id: int, dto: UpdateIngredientImageDTO) -> IngredientImage:
        ingredient_image = self.ingredient_image_repository.get_by_id(image_id)
        if not ingredient_image:
            raise ValueError("Ingredient image not found")
        
        if dto.image_url is not None:
            ingredient_image.image_url = dto.image_url
        
        return self.ingredient_image_repository.save(ingredient_image)

