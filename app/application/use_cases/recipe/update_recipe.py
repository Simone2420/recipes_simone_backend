from datetime import datetime
from app.domain.entities.recipe import Recipe
from app.domain.repositories.recipe_repository import RecipeRepository
from app.application.dtos.recipe.update_recipe_dto import UpdateRecipeDTO


class UpdateRecipeUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def execute(self, recipe_id: int, dto: UpdateRecipeDTO) -> Recipe:
        recipe = self.recipe_repository.get_by_id(recipe_id)
        if not recipe:
            raise ValueError("Recipe not found")
        
        if dto.title is not None:
            recipe.title = dto.title
        if dto.description is not None:
            recipe.description = dto.description
        if dto.status is not None:
            recipe.status = dto.status
        if dto.dificulty_id is not None:
            recipe.dificulty_id = dto.dificulty_id
        
        recipe.updated_at = datetime.utcnow()
        
        return self.recipe_repository.save(recipe)

