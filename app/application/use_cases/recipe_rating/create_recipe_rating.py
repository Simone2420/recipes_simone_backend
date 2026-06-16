from app.domain.entities.recipe_rating import RecipeRating
from app.domain.repositories.recipe_rating_repository import RecipeRatingRepository
from app.application.dtos.recipe_rating.create_recipe_rating_dto import CreateRecipeRatingDTO


class CreateRecipeRatingUseCase:
    def __init__(self, recipe_rating_repository: RecipeRatingRepository):
        self.recipe_rating_repository = recipe_rating_repository

    def execute(self, dto: CreateRecipeRatingDTO) -> RecipeRating:
        recipe_rating = RecipeRating(
            id=0,
            value=dto.value,
            content=dto.content,
            recipe_id=dto.recipe_id,
            user_id=dto.user_id
        )
        return self.recipe_rating_repository.save(recipe_rating)

