from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.recipe import Recipe


class RecipeRepository(ABC):
    @abstractmethod
    def get_by_id(self, recipe_id: int) -> Optional[Recipe]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Recipe]:
        pass
    
    @abstractmethod
    def get_by_user_id(self, user_id: int) -> List[Recipe]:
        pass
    
    @abstractmethod
    def save(self, recipe: Recipe) -> Recipe:
        pass
    
    @abstractmethod
    def delete(self, recipe_id: int) -> None:
        pass

