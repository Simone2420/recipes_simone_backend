from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.ingredient import Ingredient


class IngredientRepository(ABC):
    @abstractmethod
    def get_by_id(self, ingredient_id: int) -> Optional[Ingredient]:
        pass
    
    @abstractmethod
    def get_by_recipe_id(self, recipe_id: int) -> List[Ingredient]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Ingredient]:
        pass
    
    @abstractmethod
    def save(self, ingredient: Ingredient) -> Ingredient:
        pass
    
    @abstractmethod
    def delete(self, ingredient_id: int) -> None:
        pass

