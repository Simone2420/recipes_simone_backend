from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.difficulty import Difficulty


class DifficultyRepository(ABC):
    @abstractmethod
    def get_by_id(self, difficulty_id: int) -> Optional[Difficulty]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Difficulty]:
        pass
    
    @abstractmethod
    def save(self, difficulty: Difficulty) -> Difficulty:
        pass
    
    @abstractmethod
    def delete(self, difficulty_id: int) -> None:
        pass

