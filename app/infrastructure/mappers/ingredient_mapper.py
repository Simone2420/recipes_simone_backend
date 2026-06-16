from app.domain.entities.ingredient import Ingredient
from app.infrastructure.database.models.ingredient_model import IngredientsModel


class IngredientMapper:
    @staticmethod
    def to_domain(model: IngredientsModel) -> Ingredient:
        return Ingredient(
            id=model.id,
            name=model.name,
            recipe_id=model.recipe_id
        )
    
    @staticmethod
    def to_model(entity: Ingredient) -> IngredientsModel:
        return IngredientsModel(
            id=entity.id,
            name=entity.name,
            recipe_id=entity.recipe_id
        )

