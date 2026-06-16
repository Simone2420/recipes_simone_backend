from app.domain.repositories.recipe_rating_repository import RecipeRatingRepository


class DeleteRecipeRatingUseCase:
    def __init__(self, recipe_rating_repository: RecipeRatingRepository):
        self.recipe_rating_repository = recipe_rating_repository

    def execute(self, rating_id: int) -> None:
        recipe_rating = self.recipe_rating_repository.get_by_id(rating_id)
        if not recipe_rating:
            raise ValueError("Recipe rating not found")
        
        self.recipe_rating_repository.delete(rating_id)

