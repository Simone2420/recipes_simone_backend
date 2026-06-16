from app.domain.repositories.step_repository import StepRepository


class DeleteStepUseCase:
    def __init__(self, step_repository: StepRepository):
        self.step_repository = step_repository

    def execute(self, step_id: int) -> None:
        step = self.step_repository.get_by_id(step_id)
        if not step:
            raise ValueError("Step not found")
        
        self.step_repository.delete(step_id)

