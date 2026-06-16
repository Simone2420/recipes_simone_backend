from typing import Optional
from app.domain.entities.step_image import StepImage
from app.domain.repositories.step_image_repository import StepImageRepository


class GetStepImageUseCase:
    def __init__(self, step_image_repository: StepImageRepository):
        self.step_image_repository = step_image_repository

    def execute(self, image_id: int) -> Optional[StepImage]:
        return self.step_image_repository.get_by_id(image_id)

