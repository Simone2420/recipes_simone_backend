from app.domain.entities.recipe import Recipe
from app.infrastructure.database.models.recipe_model import RecipeModel


class RecipeMapper:
    @staticmethod
    def to_domain(model: RecipeModel) -> Recipe:
        return Recipe(
            id=model.id,
            title=model.title,
            description=model.description,
            created_at=model.created_at,
            updated_at=model.updated_at,
            status=model.status,
            user_id=model.user_id,
            dificulty_id=model.dificulty_id
        )
    
    @staticmethod
    def to_model(entity: Recipe) -> RecipeModel:
        return RecipeModel(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            status=entity.status,
            user_id=entity.user_id,
            dificulty_id=entity.dificulty_id
        )

