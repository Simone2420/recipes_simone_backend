from app.domain.repositories.recipe_repository import RecipeRepository


class DeleteRecipeUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def execute(self, recipe_id: int) -> None:
        recipe = self.recipe_repository.get_by_id(recipe_id)
        if not recipe:
            raise ValueError("Recipe not found")
        
        self.recipe_repository.delete(recipe_id)

