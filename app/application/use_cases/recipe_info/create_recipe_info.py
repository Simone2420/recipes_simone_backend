from app.domain.entities.recipe_info import RecipeInfo
from app.domain.repositories.recipe_info_repository import RecipeInfoRepository
from app.application.dtos.recipe_info.create_recipe_info_dto import CreateRecipeInfoDTO


class CreateRecipeInfoUseCase:
    def __init__(self, recipe_info_repository: RecipeInfoRepository):
        self.recipe_info_repository = recipe_info_repository

    def execute(self, dto: CreateRecipeInfoDTO) -> RecipeInfo:
        recipe_info = RecipeInfo(
            id=0,
            cook_time=dto.cook_time,
            preparation_time=dto.preparation_time,
            calories=dto.calories,
            quote=dto.quote,
            recipe_id=dto.recipe_id
        )
        return self.recipe_info_repository.save(recipe_info)

