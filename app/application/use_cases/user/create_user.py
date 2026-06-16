from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.application.interfaces.password_hasher import PasswordHasher
from app.application.dtos.user.create_user_dto import CreateUserDTO


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, dto: CreateUserDTO) -> User:
        # Check if user already exists
        existing_user = self.user_repository.get_by_email(dto.email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        hashed_password = self.password_hasher.hash(dto.password)
        user = User(
            id=0,  # Will be set by the repository
            first_name=dto.first_name,
            last_name=dto.last_name,
            email=dto.email,
            hashed_password=hashed_password,
            status=True
        )
        
        return self.user_repository.save(user)

