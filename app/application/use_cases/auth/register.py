from typing import Dict, Any
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.application.interfaces.password_hasher import PasswordHasher
from app.application.interfaces.token_service import TokenService
from app.application.dtos.auth.register_dto import RegisterDTO


class RegisterUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        token_service: TokenService
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_service = token_service

    def execute(self, dto: RegisterDTO) -> Dict[str, Any]:
        existing_user = self.user_repository.get_by_email(dto.email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        hashed_password = self.password_hasher.hash(dto.password)
        user = User(
            id=0,
            first_name=dto.first_name,
            last_name=dto.last_name,
            email=dto.email,
            hashed_password=hashed_password,
            status=True
        )
        saved_user = self.user_repository.save(user)
        
        access_token = self.token_service.create_access_token(data={"sub": str(saved_user.id), "email": saved_user.email})
        refresh_token = self.token_service.create_refresh_token(data={"sub": str(saved_user.id)})
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

