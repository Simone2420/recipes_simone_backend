from sqlalchemy.orm import Session
from app.infrastructure.database.models.user_model import UserModel
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.user_role_model import UserRoleModel


class AssignRoleUseCase:
    def __init__(self, db: Session):
        self.db = db

    def execute(self, user_id: int, role_id: int) -> None:
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        
        role = self.db.query(RoleModel).filter(RoleModel.id == role_id).first()
        if not role:
            raise ValueError("Role not found")
        
        # Check if already assigned
        existing = self.db.query(UserRoleModel).filter(
            UserRoleModel.user_id == user_id,
            UserRoleModel.role_id == role_id
        ).first()
        
        if existing:
            return  # Already assigned
        
        user_role = UserRoleModel(user_id=user_id, role_id=role_id)
        self.db.add(user_role)
        self.db.commit()

