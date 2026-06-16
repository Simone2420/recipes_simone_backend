from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.comment import Comment


class CommentRepository(ABC):
    @abstractmethod
    def get_by_id(self, comment_id: int) -> Optional[Comment]:
        pass
    
    @abstractmethod
    def get_by_recipe_id(self, recipe_id: int) -> List[Comment]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Comment]:
        pass
    
    @abstractmethod
    def save(self, comment: Comment) -> Comment:
        pass
    
    @abstractmethod
    def delete(self, comment_id: int) -> None:
        pass

