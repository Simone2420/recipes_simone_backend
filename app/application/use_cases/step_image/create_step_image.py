from app.domain.entities.step_image import StepImage
from app.domain.repositories.step_image_repository import StepImageRepository
from app.application.dtos.step_image.create_step_image_dto import CreateStepImageDTO


class CreateStepImageUseCase:
    def __init__(self, step_image_repository: StepImageRepository):
        self.step_image_repository = step_image_repository

    def execute(self, dto: CreateStepImageDTO) -> StepImage:
        step_image = StepImage(
            id=0,
            image_url=dto.image_url,
            order=dto.order,
            step_id=dto.step_id
        )
        return self.step_image_repository.save(step_image)

