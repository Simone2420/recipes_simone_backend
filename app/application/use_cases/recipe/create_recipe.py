from datetime import datetime
from app.domain.entities.recipe import Recipe
from app.domain.repositories.recipe_repository import RecipeRepository
from app.application.dtos.recipe.create_recipe_dto import CreateRecipeDTO


class CreateRecipeUseCase:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def execute(self, dto: CreateRecipeDTO) -> Recipe:
        now = datetime.utcnow()
        recipe = Recipe(
            id=0,
            title=dto.title,
            description=dto.description,
            created_at=now,
            updated_at=now,
            status=True,
            user_id=dto.user_id,
            dificulty_id=dto.dificulty_id
        )
        return self.recipe_repository.save(recipe)

