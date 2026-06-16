from app.domain.entities.recipe_image import RecipeImage
from app.infrastructure.database.models.recipe_image_model import RecipeImageModel


class RecipeImageMapper:
    @staticmethod
    def to_domain(model: RecipeImageModel) -> RecipeImage:
        return RecipeImage(
            id=model.id,
            image_url=model.image_url,
            recipe_id=model.recipe_id
        )
    
    @staticmethod
    def to_model(entity: RecipeImage) -> RecipeImageModel:
        return RecipeImageModel(
            id=entity.id,
            image_url=entity.image_url,
            recipe_id=entity.recipe_id
        )

