from app.domain.entities.recipe_rating import RecipeRating
from app.infrastructure.database.models.recipe_rating_model import RecipeRatingModel


class RecipeRatingMapper:
    @staticmethod
    def to_domain(model: RecipeRatingModel) -> RecipeRating:
        return RecipeRating(
            id=model.id,
            value=model.value,
            content=model.content,
            recipe_id=model.recipe_id,
            user_id=model.user_id
        )
    
    @staticmethod
    def to_model(entity: RecipeRating) -> RecipeRatingModel:
        return RecipeRatingModel(
            id=entity.id,
            value=entity.value,
            content=entity.content,
            recipe_id=entity.recipe_id,
            user_id=entity.user_id
        )

