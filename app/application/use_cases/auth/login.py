from typing import Dict, Any
from app.domain.repositories.user_repository import UserRepository
from app.application.interfaces.password_hasher import PasswordHasher
from app.application.interfaces.token_service import TokenService
from app.application.dtos.auth.login_dto import LoginDTO


class LoginUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        token_service: TokenService
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_service = token_service

    def execute(self, dto: LoginDTO) -> Dict[str, Any]:
        user = self.user_repository.get_by_email(dto.email)
        if not user:
            raise ValueError("Invalid email or password")
        
        if not self.password_hasher.verify(dto.password, user.hashed_password):
            raise ValueError("Invalid email or password")
        
        if not user.status:
            raise ValueError("User is inactive")
        
        access_token = self.token_service.create_access_token(data={"sub": str(user.id), "email": user.email})
        refresh_token = self.token_service.create_refresh_token(data={"sub": str(user.id)})
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

