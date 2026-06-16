from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.recipe_rating import RecipeRating


class RecipeRatingRepository(ABC):
    @abstractmethod
    def get_by_id(self, rating_id: int) -> Optional[RecipeRating]:
        pass
    
    @abstractmethod
    def get_by_recipe_id(self, recipe_id: int) -> List[RecipeRating]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[RecipeRating]:
        pass
    
    @abstractmethod
    def save(self, rating: RecipeRating) -> RecipeRating:
        pass
    
    @abstractmethod
    def delete(self, rating_id: int) -> None:
        pass

