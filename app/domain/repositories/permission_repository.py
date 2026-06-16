from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.permission import Permission


class PermissionRepository(ABC):
    @abstractmethod
    def get_by_id(self, permission_id: int) -> Optional[Permission]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Permission]:
        pass
    
    @abstractmethod
    def save(self, permission: Permission) -> Permission:
        pass
    
    @abstractmethod
    def delete(self, permission_id: int) -> None:
        pass

