from app.domain.entities.step import Step
from app.domain.repositories.step_repository import StepRepository
from app.application.dtos.step.create_step_dto import CreateStepDTO


class CreateStepUseCase:
    def __init__(self, step_repository: StepRepository):
        self.step_repository = step_repository

    def execute(self, dto: CreateStepDTO) -> Step:
        step = Step(
            id=0,
            content=dto.content,
            description=dto.description,
            order=dto.order,
            recipe_id=dto.recipe_id
        )
        return self.step_repository.save(step)

