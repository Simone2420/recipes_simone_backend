from abc import ABC, abstractmethod
from typing import Dict, Any


class TokenService(ABC):
    @abstractmethod
    def create_access_token(self, data: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def create_refresh_token(self, data: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def decode_token(self, token: str) -> Dict[str, Any]:
        pass

