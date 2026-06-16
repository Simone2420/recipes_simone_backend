from typing import List
from app.domain.entities.step_image import StepImage
from app.domain.repositories.step_image_repository import StepImageRepository


class ListStepImagesByStepUseCase:
    def __init__(self, step_image_repository: StepImageRepository):
        self.step_image_repository = step_image_repository

    def execute(self, step_id: int) -> List[StepImage]:
        return self.step_image_repository.get_by_step_id(step_id)

