from typing import List
from app.domain.entities.recipe_rating import RecipeRating
from app.domain.repositories.recipe_rating_repository import RecipeRatingRepository


class ListRecipeRatingsByRecipeUseCase:
    def __init__(self, recipe_rating_repository: RecipeRatingRepository):
        self.recipe_rating_repository = recipe_rating_repository

    def execute(self, recipe_id: int) -> List[RecipeRating]:
        return self.recipe_rating_repository.get_by_recipe_id(recipe_id)

