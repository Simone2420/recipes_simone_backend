from app.domain.entities.recipe_rating import RecipeRating
from app.domain.repositories.recipe_rating_repository import RecipeRatingRepository
from app.application.dtos.recipe_rating.update_recipe_rating_dto import UpdateRecipeRatingDTO


class UpdateRecipeRatingUseCase:
    def __init__(self, recipe_rating_repository: RecipeRatingRepository):
        self.recipe_rating_repository = recipe_rating_repository

    def execute(self, rating_id: int, dto: UpdateRecipeRatingDTO) -> RecipeRating:
        recipe_rating = self.recipe_rating_repository.get_by_id(rating_id)
        if not recipe_rating:
            raise ValueError("Recipe rating not found")
        
        if dto.value is not None:
            recipe_rating.value = dto.value
        if dto.content is not None:
            recipe_rating.content = dto.content
        
        return self.recipe_rating_repository.save(recipe_rating)

