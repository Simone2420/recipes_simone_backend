from app.domain.entities.difficulty import Difficulty
from app.domain.repositories.difficulty_repository import DifficultyRepository
from app.application.dtos.difficulty.create_difficulty_dto import CreateDifficultyDTO


class CreateDifficultyUseCase:
    def __init__(self, difficulty_repository: DifficultyRepository):
        self.difficulty_repository = difficulty_repository

    def execute(self, dto: CreateDifficultyDTO) -> Difficulty:
        difficulty = Difficulty(
            id=0,
            name=dto.name
        )
        return self.difficulty_repository.save(difficulty)

