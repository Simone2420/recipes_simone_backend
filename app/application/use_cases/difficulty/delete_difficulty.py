from app.domain.repositories.difficulty_repository import DifficultyRepository


class DeleteDifficultyUseCase:
    def __init__(self, difficulty_repository: DifficultyRepository):
        self.difficulty_repository = difficulty_repository

    def execute(self, difficulty_id: int) -> None:
        difficulty = self.difficulty_repository.get_by_id(difficulty_id)
        if not difficulty:
            raise ValueError("Difficulty not found")
        
        self.difficulty_repository.delete(difficulty_id)

