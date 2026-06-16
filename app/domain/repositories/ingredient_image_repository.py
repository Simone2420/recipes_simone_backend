from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.ingredient_image import IngredientImage


class IngredientImageRepository(ABC):
    @abstractmethod
    def get_by_id(self, image_id: int) -> Optional[IngredientImage]:
        pass
    
    @abstractmethod
    def get_by_ingredient_id(self, ingredient_id: int) -> List[IngredientImage]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[IngredientImage]:
        pass
    
    @abstractmethod
    def save(self, image: IngredientImage) -> IngredientImage:
        pass
    
    @abstractmethod
    def delete(self, image_id: int) -> None:
        pass

