from app.domain.repositories.recipe_info_repository import RecipeInfoRepository


class DeleteRecipeInfoUseCase:
    def __init__(self, recipe_info_repository: RecipeInfoRepository):
        self.recipe_info_repository = recipe_info_repository

    def execute(self, info_id: int) -> None:
        recipe_info = self.recipe_info_repository.get_by_id(info_id)
        if not recipe_info:
            raise ValueError("Recipe info not found")
        
        self.recipe_info_repository.delete(info_id)

