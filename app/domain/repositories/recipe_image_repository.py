from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.recipe_image import RecipeImage


class RecipeImageRepository(ABC):
    @abstractmethod
    def get_by_id(self, image_id: int) -> Optional[RecipeImage]:
        pass
    
    @abstractmethod
    def get_by_recipe_id(self, recipe_id: int) -> List[RecipeImage]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[RecipeImage]:
        pass
    
    @abstractmethod
    def save(self, image: RecipeImage) -> RecipeImage:
        pass
    
    @abstractmethod
    def delete(self, image_id: int) -> None:
        pass

