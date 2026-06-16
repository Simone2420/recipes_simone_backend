from app.domain.entities.recipe_info import RecipeInfo
from app.infrastructure.database.models.recipe_info_model import RecipeInfoModel


class RecipeInfoMapper:
    @staticmethod
    def to_domain(model: RecipeInfoModel) -> RecipeInfo:
        return RecipeInfo(
            id=model.id,
            cook_time=model.cook_time,
            preparation_time=model.preparation_time,
            calories=model.calories,
            quote=model.quote,
            recipe_id=model.recipe_id
        )
    
    @staticmethod
    def to_model(entity: RecipeInfo) -> RecipeInfoModel:
        return RecipeInfoModel(
            id=entity.id,
            cook_time=entity.cook_time,
            preparation_time=entity.preparation_time,
            calories=entity.calories,
            quote=entity.quote,
            recipe_id=entity.recipe_id
        )

