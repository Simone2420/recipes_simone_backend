from typing import Dict, Any
from app.domain.repositories.user_repository import UserRepository
from app.application.interfaces.token_service import TokenService


class RefreshTokenUseCase:
    def __init__(self, user_repository: UserRepository, token_service: TokenService):
        self.user_repository = user_repository
        self.token_service = token_service

    def execute(self, refresh_token: str) -> Dict[str, Any]:
        payload = self.token_service.decode_token(refresh_token)
        user_id = int(payload.get("sub"))
        
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        if not user.status:
            raise ValueError("User is inactive")
        
        access_token = self.token_service.create_access_token(data={"sub": str(user.id), "email": user.email})
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

