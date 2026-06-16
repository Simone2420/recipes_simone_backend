from app.domain.entities.difficulty import Difficulty
from app.domain.repositories.difficulty_repository import DifficultyRepository
from app.application.dtos.difficulty.update_difficulty_dto import UpdateDifficultyDTO


class UpdateDifficultyUseCase:
    def __init__(self, difficulty_repository: DifficultyRepository):
        self.difficulty_repository = difficulty_repository

    def execute(self, difficulty_id: int, dto: UpdateDifficultyDTO) -> Difficulty:
        difficulty = self.difficulty_repository.get_by_id(difficulty_id)
        if not difficulty:
            raise ValueError("Difficulty not found")
        
        if dto.name is not None:
            difficulty.name = dto.name
        
        return self.difficulty_repository.save(difficulty)

