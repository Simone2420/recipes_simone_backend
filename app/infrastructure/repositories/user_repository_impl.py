from typing import List, Optional
from sqlalchemy.orm import Session
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.mappers.user_mapper import UserMapper


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        model = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not model:
            return None
        return UserMapper.to_domain(model)
    
    def get_by_email(self, email: str) -> Optional[User]:
        model = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not model:
            return None
        return UserMapper.to_domain(model)
    
    def get_all(self) -> List[User]:
        models = self.db.query(UserModel).all()
        return [UserMapper.to_domain(model) for model in models]
    
    def save(self, user: User) -> User:
        if user.id:
            model = self.db.query(UserModel).filter(UserModel.id == user.id).first()
            if model:
                model.first_name = user.first_name
                model.last_name = user.last_name
                model.email = user.email
                model.hashed_password = user.hashed_password
                model.status = user.status
            else:
                model = UserMapper.to_model(user)
                self.db.add(model)
                self.db.flush()
        else:
            model = UserMapper.to_model(user)
            self.db.add(model)
            self.db.flush()
        
        self.db.commit()
        return UserMapper.to_domain(model)
    
    def delete(self, user_id: int) -> None:
        model = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if model:
            self.db.delete(model)
            self.db.commit()

