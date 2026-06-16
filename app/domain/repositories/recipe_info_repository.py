from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.recipe_info import RecipeInfo


class RecipeInfoRepository(ABC):
    @abstractmethod
    def get_by_id(self, info_id: int) -> Optional[RecipeInfo]:
        pass
    
    @abstractmethod
    def get_by_recipe_id(self, recipe_id: int) -> Optional[RecipeInfo]:
        pass
    
    @abstractmethod
    def save(self, info: RecipeInfo) -> RecipeInfo:
        pass
    
    @abstractmethod
    def delete(self, info_id: int) -> None:
        pass

