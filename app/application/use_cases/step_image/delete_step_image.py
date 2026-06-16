from app.domain.repositories.step_image_repository import StepImageRepository


class DeleteStepImageUseCase:
    def __init__(self, step_image_repository: StepImageRepository):
        self.step_image_repository = step_image_repository

    def execute(self, image_id: int) -> None:
        step_image = self.step_image_repository.get_by_id(image_id)
        if not step_image:
            raise ValueError("Step image not found")
        
        self.step_image_repository.delete(image_id)

