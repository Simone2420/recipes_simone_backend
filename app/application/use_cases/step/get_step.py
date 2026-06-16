from typing import Optional
from app.domain.entities.step import Step
from app.domain.repositories.step_repository import StepRepository


class GetStepUseCase:
    def __init__(self, step_repository: StepRepository):
        self.step_repository = step_repository

    def execute(self, step_id: int) -> Optional[Step]:
        return self.step_repository.get_by_id(step_id)

