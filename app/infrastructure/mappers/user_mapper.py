from app.domain.entities.user import User
from app.infrastructure.database.models.user_model import UserModel


class UserMapper:
    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            hashed_password=model.hashed_password,
            status=model.status
        )
    
    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(
            id=entity.id,
            first_name=entity.first_name,
            last_name=entity.last_name,
            email=entity.email,
            hashed_password=entity.hashed_password,
            status=entity.status
        )

