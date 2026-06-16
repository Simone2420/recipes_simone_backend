from app.domain.entities.recipe_info import RecipeInfo
from app.domain.repositories.recipe_info_repository import RecipeInfoRepository
from app.application.dtos.recipe_info.update_recipe_info_dto import UpdateRecipeInfoDTO


class UpdateRecipeInfoUseCase:
    def __init__(self, recipe_info_repository: RecipeInfoRepository):
        self.recipe_info_repository = recipe_info_repository

    def execute(self, info_id: int, dto: UpdateRecipeInfoDTO) -> RecipeInfo:
        recipe_info = self.recipe_info_repository.get_by_id(info_id)
        if not recipe_info:
            raise ValueError("Recipe info not found")
        
        if dto.cook_time is not None:
            recipe_info.cook_time = dto.cook_time
        if dto.preparation_time is not None:
            recipe_info.preparation_time = dto.preparation_time
        if dto.calories is not None:
            recipe_info.calories = dto.calories
        if dto.quote is not None:
            recipe_info.quote = dto.quote
        
        return self.recipe_info_repository.save(recipe_info)

