from app.domain.entities.step import Step
from app.domain.repositories.step_repository import StepRepository
from app.application.dtos.step.update_step_dto import UpdateStepDTO


class UpdateStepUseCase:
    def __init__(self, step_repository: StepRepository):
        self.step_repository = step_repository

    def execute(self, step_id: int, dto: UpdateStepDTO) -> Step:
        step = self.step_repository.get_by_id(step_id)
        if not step:
            raise ValueError("Step not found")
        
        if dto.content is not None:
            step.content = dto.content
        if dto.description is not None:
            step.description = dto.description
        if dto.order is not None:
            step.order = dto.order
        
        return self.step_repository.save(step)

