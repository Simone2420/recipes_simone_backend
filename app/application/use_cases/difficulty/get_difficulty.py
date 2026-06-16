from typing import Optional
from app.domain.entities.difficulty import Difficulty
from app.domain.repositories.difficulty_repository import DifficultyRepository


class GetDifficultyUseCase:
    def __init__(self, difficulty_repository: DifficultyRepository):
        self.difficulty_repository = difficulty_repository

    def execute(self, difficulty_id: int) -> Optional[Difficulty]:
        return self.difficulty_repository.get_by_id(difficulty_id)

