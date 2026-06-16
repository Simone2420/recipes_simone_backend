from app.domain.entities.ingredient_image import IngredientImage
from app.infrastructure.database.models.ingredient_image_model import IngredientImageModel


class IngredientImageMapper:
    @staticmethod
    def to_domain(model: IngredientImageModel) -> IngredientImage:
        return IngredientImage(
            id=model.id,
            image_url=model.image_url,
            ingredient_id=model.ingredient_id
        )
    
    @staticmethod
    def to_model(entity: IngredientImage) -> IngredientImageModel:
        return IngredientImageModel(
            id=entity.id,
            image_url=entity.image_url,
            ingredient_id=entity.ingredient_id
        )

