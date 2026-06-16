from typing import Optional
from app.domain.entities.recipe_info import RecipeInfo
from app.domain.repositories.recipe_info_repository import RecipeInfoRepository


class GetRecipeInfoByRecipeUseCase:
    def __init__(self, recipe_info_repository: RecipeInfoRepository):
        self.recipe_info_repository = recipe_info_repository

    def execute(self, recipe_id: int) -> Optional[RecipeInfo]:
        return self.recipe_info_repository.get_by_recipe_id(recipe_id)

