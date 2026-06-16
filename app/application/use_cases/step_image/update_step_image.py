from app.domain.entities.step_image import StepImage
from app.domain.repositories.step_image_repository import StepImageRepository
from app.application.dtos.step_image.update_step_image_dto import UpdateStepImageDTO


class UpdateStepImageUseCase:
    def __init__(self, step_image_repository: StepImageRepository):
        self.step_image_repository = step_image_repository

    def execute(self, image_id: int, dto: UpdateStepImageDTO) -> StepImage:
        step_image = self.step_image_repository.get_by_id(image_id)
        if not step_image:
            raise ValueError("Step image not found")
        
        if dto.image_url is not None:
            step_image.image_url = dto.image_url
        if dto.order is not None:
            step_image.order = dto.order
        
        return self.step_image_repository.save(step_image)

