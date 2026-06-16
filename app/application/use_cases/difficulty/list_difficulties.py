from typing import List
from app.domain.entities.difficulty import Difficulty
from app.domain.repositories.difficulty_repository import DifficultyRepository


class ListDifficultiesUseCase:
    def __init__(self, difficulty_repository: DifficultyRepository):
        self.difficulty_repository = difficulty_repository

    def execute(self) -> List[Difficulty]:
        return self.difficulty_repository.get_all()

