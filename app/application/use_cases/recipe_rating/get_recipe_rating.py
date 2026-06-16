from typing import Optional
from app.domain.entities.recipe_rating import RecipeRating
from app.domain.repositories.recipe_rating_repository import RecipeRatingRepository


class GetRecipeRatingUseCase:
    def __init__(self, recipe_rating_repository: RecipeRatingRepository):
        self.recipe_rating_repository = recipe_rating_repository

    def execute(self, rating_id: int) -> Optional[RecipeRating]:
        return self.recipe_rating_repository.get_by_id(rating_id)

