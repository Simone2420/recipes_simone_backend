from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.step_image import StepImage


class StepImageRepository(ABC):
    @abstractmethod
    def get_by_id(self, image_id: int) -> Optional[StepImage]:
        pass
    
    @abstractmethod
    def get_by_step_id(self, step_id: int) -> List[StepImage]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[StepImage]:
        pass
    
    @abstractmethod
    def save(self, image: StepImage) -> StepImage:
        pass
    
    @abstractmethod
    def delete(self, image_id: int) -> None:
        pass

