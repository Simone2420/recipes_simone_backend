from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.role import Role


class RoleRepository(ABC):
    @abstractmethod
    def get_by_id(self, role_id: int) -> Optional[Role]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Role]:
        pass
    
    @abstractmethod
    def save(self, role: Role) -> Role:
        pass
    
    @abstractmethod
    def delete(self, role_id: int) -> None:
        pass

