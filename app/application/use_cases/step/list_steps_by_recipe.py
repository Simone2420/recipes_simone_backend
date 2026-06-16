from typing import List
from app.domain.entities.step import Step
from app.domain.repositories.step_repository import StepRepository


class ListStepsByRecipeUseCase:
    def __init__(self, step_repository: StepRepository):
        self.step_repository = step_repository

    def execute(self, recipe_id: int) -> List[Step]:
        return self.step_repository.get_by_recipe_id(recipe_id)

