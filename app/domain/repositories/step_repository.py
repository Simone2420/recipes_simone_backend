from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.step import Step


class StepRepository(ABC):
    @abstractmethod
    def get_by_id(self, step_id: int) -> Optional[Step]:
        pass
    
    @abstractmethod
    def get_by_recipe_id(self, recipe_id: int) -> List[Step]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Step]:
        pass
    
    @abstractmethod
    def save(self, step: Step) -> Step:
        pass
    
    @abstractmethod
    def delete(self, step_id: int) -> None:
        pass

