from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.application.interfaces.password_hasher import PasswordHasher
from app.application.dtos.user.update_user_dto import UpdateUserDTO


class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, user_id: int, dto: UpdateUserDTO) -> User:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        if dto.first_name is not None:
            user.first_name = dto.first_name
        if dto.last_name is not None:
            user.last_name = dto.last_name
        if dto.email is not None:
            # Check if email is already taken by another user
            existing_user = self.user_repository.get_by_email(dto.email)
            if existing_user and existing_user.id != user_id:
                raise ValueError("Email already taken")
            user.email = dto.email
        if dto.password is not None:
            user.hashed_password = self.password_hasher.hash(dto.password)
        if dto.status is not None:
            user.status = dto.status
        
        return self.user_repository.save(user)

